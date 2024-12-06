import math
import numpy as np

def test_get_radec():
    
    """This test file tests if the get_radec() function from sky_sim_better_styled.py correctly converts the coordinates of the centre of the Andromeda galaxy to degrees correctly."""

    def get_radec():
        # from wikipedia
        andromeda_ra = '00:42:44.3'
        andromeda_dec = '41:16:09'

        degrees, minutes, seconds = andromeda_dec.split(':')
        dec = int(degrees)+int(minutes)/60+float(seconds)/3600

        hours, minutes, seconds = andromeda_ra.split(':')
        ra = 15*(int(hours)+int(minutes)/60+float(seconds)/3600)
        ra = ra/math.cos(dec*math.pi/180)
        return ra, dec

    central_ra, central_dec = get_radec()

    np.testing.assert_array_almost_equal_nulp(central_ra, 14.215420962967535)
    np.testing.assert_array_almost_equal_nulp(central_dec, 41.26916666666667)
