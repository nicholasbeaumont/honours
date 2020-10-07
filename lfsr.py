# Seed the register and initialise the keystream array.
# Initialise the lfsr by creating a copy of the seed.
# TODO: seed the register using pseudo-random number generator.
class StateGenerator:
    def __init__(self, lfsr_seed, keystream):
        self.lfsr_seed = lfsr_seed
        self.lfsr = lfsr_seed.copy()
        self.lfsr_length = len(lfsr_seed)
        self.keystream = keystream

    def myfunc(self):
        print(self.lfsr_seed)
        print(self.lfsr)
        print(self.lfsr_length)
        print(self.keystream)

    def keystream_generator(self, lfsr):
        # Calculate maximum possible clock rounds.
        max_clock_rounds = self.lfsr_length ** 2 * self.lfsr_length
        # Produce output bits and store the results in the keystream array.
        # Change the characteristic_polynomial variable to reflect the polynomial you wish to use.
        clock_rounds = 0
        while clock_rounds < max_clock_rounds:
            characteristic_polynomial = self.lfsr[0] ^ self.lfsr[3]
            output_bit = self.lfsr.pop(0)
            self.keystream.append(output_bit)
            feedback_bit = characteristic_polynomial
            lfsr.insert(self.lfsr_length-1, feedback_bit)
            clock_rounds += 1

        # Print the results.
        value = input('Please entre the characteristic polynomial: ')
        print('The characteristic polynomial is {0}'.format(value))
        print('The register seed is {0}'.format(self.lfsr_seed))
        print('The register state after {0} clocks is {1}'.format(
            clock_rounds, self.lfsr))
        print('The keystream is {0}'.format(self.keystream))

        return self.keystream

    def ones_and_zeros(self, keystream):
        zeros_tally = 0
        zeros_percentage = 0
        ones_tally = 0
        ones_percentage = 0

        for x in keystream:
            if keystream[x] == 0:
                zeros_tally += 1
            else:
                ones_tally += 1

        zeros_percentage = zeros_tally / len(keystream) * 100
        ones_percentage = ones_tally / len(keystream) * 100
        print('There are {0} zeros in the keystream, or {1}%.'.format(
            zeros_tally, zeros_percentage))
        print('There are {0} ones in the keystream, or {1}%.'.format(
            ones_tally, ones_percentage))

    def convert_to_2d(self, keystream):
        two_dimensional_list = []
        start_slice = 0
        finish_slice = self.lfsr_length
        for i in range(len(keystream)):
            if i > 0 and (i+1) % self.lfsr_length == 0:
                two_dimensional_list.append(
                    keystream[start_slice:finish_slice])
                start_slice = finish_slice
                finish_slice += self.lfsr_length
        print(two_dimensional_list)
        return two_dimensional_list


lfsr0 = StateGenerator([0, 1, 0, 1], [])
# seed_lfsr()
lfsr0.ones_and_zeros(lfsr0.keystream_generator(lfsr0.lfsr))
new_array = lfsr0.convert_to_2d(lfsr0.keystream)
if new_array[0] == new_array[14]:
    print('there is a match')
else:
    print('there is no match')
# TODO: statistical analysis.
