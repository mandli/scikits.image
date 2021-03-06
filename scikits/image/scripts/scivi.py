"""scikits.image viewer"""
def main():
    import scikits.image.io as io
    import sys

    if len(sys.argv) != 2:
        print "Usage: scivi <image-file>"
        sys.exit(-1)

    io.use_plugin('qt')
    io.imshow(io.imread(sys.argv[1]), fancy=True)
    io.show()

