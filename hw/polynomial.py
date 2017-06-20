# The start of a very basic Polynomial class...
class Polynomial(object):
    def __init__(self, coeffs):
        # if coeffs == [2,-3,5]:  2x**2-3*x+5
        # @TODO: eliminate leading zero's
        self.coeffs = coeffs
    
    def degree(self):
        # The degree is power of the largest exponent, and since
        # we start at x**0, this is one less than the number of coefficients.
        return len(self.coeffs)-1
    
    def coeff(self, power):
        # This returns the coefficient corresponding to the given power.
        # Note that these are stored in reverse, in that the coefficient
        # for x**0 is not stored in coeffs[0] but rather coeffs[-1].
        return self.coeffs[self.degree()-power]
    
    def evalAt(self, x):
        # Evaluate this polynomial at the given value of x.
        return sum([self.coeff(power)*x**power
                    for power in range(self.degree()+1)])

    def __add__(self, other):
        # Add this polynomial to another polynomial, producing a third
        # polyonial as the result.  This makes the + operator work right.
        # First, make both coefficent lists the same length by nondestructively
        # adding 0's to the front of the shorter one
        (coeffs1, coeffs2) = (self.coeffs, other.coeffs)
        if (len(coeffs1) > len(coeffs2)):
            (coeffs1, coeffs2) = (coeffs2, coeffs1)
        # Now, coeffs1 is shorter, so add 0's to its front
        coeffs1 = [0]*(len(coeffs2)-len(coeffs1)) + coeffs1
        # Now they are the same length, so add them to get the new coefficients
        coeffs = [coeffs1[i] + coeffs2[i] for i in range(len(coeffs1))]
        # And create the new Polynomial instance with these new coefficients
        return Polynomial(coeffs)

    def __str__(self):
        # Convert this polynomial into a human-readable string.
        # This is not a very good string implementation. Ugly, but functional.
        result = ""
        for power in xrange(self.degree(), -1, -1):
            if (result != ""): result += "+"
            coeff = self.coeff(power)
            result += "%d*x**%d" % (coeff, power)
        return result