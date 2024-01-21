# This function will return the probability of finding the TV remote given the probability of being comfy on the couch
def ProbabilityOfFindingTheTVRemote(the_probability_your_butt_is_comfy_on_the_couch = 0.0):
    # If you are standing and trying... you'll eventually find it.
    the_probability_of_finding_the_tv_remote = 1 #  100%
	
	# But... as the_probability_your_butt_is_comfy_on_the_couch approaches 1 (100%)
	# the_probability_of_finding_the_tv_remote approaches 0 (0%)
    the_probability_of_finding_the_tv_remote = 1 - the_probability_your_butt_is_comfy_on_the_couch
	
    # report the probability of finding the TV remote
    return the_probability_of_finding_the_tv_remote


# So given the probability of finding oneself comfy on the couch
# and changing our probability of being comfy on the couch by 5% each time
# Let's ask, what is the probability of finding the TV remote?
for i in range(0, 105, 5):
    # I am i percent comfy on the couch
    # so let p be the probability of finding the TV remote
    p = ProbabilityOfFindingTheTVRemote(i/100.0)
    # therefore...
    print("The probability of finding the TV remote is "+ str(round(p*100, 2)) +"% when I am " + str(i) + "% likely to be comfy on the couch.")

# The probability of finding the TV remote is 100.0% when I am 0% likely to be comfy on the couch.
# The probability of finding the TV remote is 95.0% when I am 5% likely to be comfy on the couch.
# The probability of finding the TV remote is 90.0% when I am 10% likely to be comfy on the couch.
# The probability of finding the TV remote is 85.0% when I am 15% likely to be comfy on the couch.
# The probability of finding the TV remote is 80.0% when I am 20% likely to be comfy on the couch.
# The probability of finding the TV remote is 75.0% when I am 25% likely to be comfy on the couch.
# The probability of finding the TV remote is 70.0% when I am 30% likely to be comfy on the couch.
# The probability of finding the TV remote is 65.0% when I am 35% likely to be comfy on the couch.
# The probability of finding the TV remote is 60.0% when I am 40% likely to be comfy on the couch.
# The probability of finding the TV remote is 55.0% when I am 45% likely to be comfy on the couch.
# The probability of finding the TV remote is 50.0% when I am 50% likely to be comfy on the couch.
# The probability of finding the TV remote is 45.0% when I am 55% likely to be comfy on the couch.
# The probability of finding the TV remote is 40.0% when I am 60% likely to be comfy on the couch.
# The probability of finding the TV remote is 35.0% when I am 65% likely to be comfy on the couch.
# The probability of finding the TV remote is 30.0% when I am 70% likely to be comfy on the couch.
# The probability of finding the TV remote is 25.0% when I am 75% likely to be comfy on the couch.
# The probability of finding the TV remote is 20.0% when I am 80% likely to be comfy on the couch.
# The probability of finding the TV remote is 15.0% when I am 85% likely to be comfy on the couch.
# The probability of finding the TV remote is 10.0% when I am 90% likely to be comfy on the couch.
# The probability of finding the TV remote is 5.0% when I am 95% likely to be comfy on the couch.
# The probability of finding the TV remote is 0.0% when I am 100% likely to be comfy on the couch.
