
def levels(clip, gamma):
    """ Adjust levels of a video clip """
    def fl(im):
        corrected = 20 + (235*(1.0*im/255)**gamma)
        return corrected.astype('uint8')
    
    return clip.fl_image(fl)
