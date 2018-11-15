"""Planet class demonstrating the use of self-calling methods.
"""


class Planet(object):

    def rotate(self):
        """Prints rotate.
        """
        print('Rotate')

    def revolve(self):
        """Prints revolve.
        """
        print('Revolve')

    def rotate_and_revolve(self):
        """Calls functions rotate() and revolve()
        """
        self.rotate()
        self.revolve()


earth = Planet()
earth.rotate()
earth.revolve()
earth.rotate_and_revolve()
