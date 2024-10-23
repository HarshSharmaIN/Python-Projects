from tkinter import *
from tkinter import filedialog, messagebox
import cv2
import numpy as np
import PIL.Image
import PIL.ImageTk
import matplotlib.pyplot as plt
from skimage import exposure

class Editor(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('Image Editor')
        self.resizable(0, 0)

        self.imageLabel = Label(self)
        self.imageLabel.grid(row=0, column=0)

        self.openImage('flower.jpg') #default image

        self.butFrame = Frame(self)
        self.butFrame.grid(row=0, column=1)

        self.buttonQuit = Button(self.butFrame, text='Quit', command=self.quit).pack(fill=BOTH)
        self.buttonOpen = Button(self.butFrame, text='Open image', command=self.openImage).pack(fill=BOTH)
        self.buttonRevert = Button(self.butFrame, text='Revert to original', command=self.revertImage).pack(fill=BOTH)
        self.buttonSave = Button(self.butFrame, text='Save image', command=self.saveImage).pack(fill=BOTH)

        self.buttonHist = Button(self.butFrame, text='Histogram', command=self.histogram).pack(fill=BOTH)
        self.buttonEqualize = Button(self.butFrame, text='Equalize Histogram', command=self.equalizeHistograms).pack(fill=BOTH)
        self.buttonMatch = Button(self.butFrame, text='Match Histograms', command=self.matchHistograms).pack(fill=BOTH)

    def updateLabel(self, img):
        tempImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        tempImg = PIL.Image.fromarray(tempImg)
        tempImg = PIL.ImageTk.PhotoImage(image=tempImg)
        self.imageLabel.configure(image=tempImg)
        self.imageLabel.image = tempImg

    def openImage(self, filename=None):
        if filename is None:
            try:
                filename = filedialog.askopenfilename(initialdir='~/Pictures', title='Open image')
            except (OSError, FileNotFoundError):
                messagebox.showerror('Error', 'Unable to find or open file <filename>')
            except Exception as error:
                messagebox.showerror('Error', f'An error occurred: {error}')

        if filename:
            self.image = cv2.imread(filename)
            self.origImage = self.image.copy()
            self.updateLabel(self.image)

    def revertImage(self):
        self.image = self.origImage.copy()
        self.updateLabel(self.image)

    def saveImage(self):
        try:
            filename = filedialog.asksaveasfilename(initialdir='~/Pictures', title='Save image')
        except Exception as error:
            messagebox.showerror('Error', f'An error occurred: {error}')

        if filename:
            cv2.imwrite(filename, self.image)

    def histogram(self):
        if len(self.image.shape) == 3:  # Color image
            color = ('b', 'g', 'r')
            for i, col in enumerate(color):
                hist = cv2.calcHist([self.image], [i], None, [256], [0, 256])
                plt.plot(hist, color=col)
                plt.xlim([0, 256])
        else:  # Grayscale image
            hist = cv2.calcHist([self.image], [0], None, [256], [0, 256])
            plt.plot(hist, color='k')
            plt.xlim([0, 256])

        plt.title('Histogram')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
        plt.show()

    def equalizeHistograms(self):
        #check if greyscale, if yes directly apply histogram equalization
        if len(self.image.shape) == 2:
            equalized_image = cv2.equalizeHist(self.image)
        else:
            #for colour images, euqlize each channel seperately
            ycrcb_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2YCrCb)
            ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])
            #convert back to BGR colour space
            equalized_image = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)
        
        self.image = equalized_image
        self.updateLabel(self.image)

    def matchHistograms(self):
        #reference image to match the histogram with 
        reference_filename = filedialog.askopenfilename(title='Reference image')
        if reference_filename:
            reference_image = cv2.imread(reference_filename)

            if reference_image.shape[-1] != self.image.shape[-1]:
                messagebox.showerror("Error", "The reference image must have the same number of channels as the current image.")
                return

            if len(self.image.shape) == 3:
                matched = exposure.match_histograms(self.image, reference_image, channel_axis=-1)
            else:
                matched = exposure.match_histograms(self.image, reference_image)

            matched = (matched * 255).astype(np.uint8)
            self.image = matched
            self.updateLabel(self.image)

editor = Editor()
editor.mainloop()
