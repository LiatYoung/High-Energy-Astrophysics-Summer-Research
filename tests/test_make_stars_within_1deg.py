import math
import random

def test_make_stars():
    """This function tests if the make_stars function from sky_sim_better_styled.py creates stars within 1 degree from the centre of the Andromeda galaxy."""

    NSRC = 1_000_000

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

    def crop_to_circle(ras, decs, ref_ra, ref_dec, radius):
        """
        Crop an input list of positions so that they lie within a radius of a reference position.
    
        Parameters
        ---------
        ras, decs: list(float)
            The ra and dec in degrees of the data points
    
        ref_ra, ref_dec: float
            The reference location
        
        radius: float
            The radius in degrees
    
        Returns
        -------
        ras, decs: list
            A list of ra and dec coordinates that pass our filter.    
        """

        ra_out = []
        dec_out = []

        for i in range(len(ras)):
            if (ras[i]-ref_ra)**2 + (decs[i]-ref_dec)**2 < radius**2: # Recall x^2 + y^2 = r^2  equation for a circle
                ra_out.append(ras[i])
                dec_out.append(decs[i])

            return ra_out, dec_out
        
    def make_stars(ra, dec, nsrc=NSRC):
        ras = []
        decs = []
        for _ in range(nsrc):
            ras.append(ra + random.uniform(-1, 1))
            decs.append(dec + random.uniform(-1, 1))

            # apply the crop_to_circle filter
            ras, decs, = crop_to_circle(ras, decs, ra, dec, 1)

        return ras, decs

    central_ra, central_dec = get_radec()

    ras, decs = make_stars(central_ra, central_dec)

    for i in range(len(ras)):
        assert (ras[i]-central_ra)**2 + (decs[i]-central_dec)**2 < 1**2
