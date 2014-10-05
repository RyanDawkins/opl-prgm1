# This class is abstracted for later implementation
class Storage(object):
    # We are forcing the implementation of these methods so that we can
    # call them later on in the console class using the execute method.
    def store(self, name, age, gpa, grade):
        raise NotImplementedError( "Should have implemented this" )
    def delete(self, name):
        raise NotImplementedError( "Should have implemented this" )
    def list(self):
        raise NotImplementedError( "Should have implemented this" )
