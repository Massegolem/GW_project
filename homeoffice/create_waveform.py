import pylab
from pycbc.waveform import get_fd_waveform

# GW250114-like parameters
m1 = 33.6       # solar masses
m2 = 32.2       # solar masses
distance = 403  # Mpc
inclination = 0.78  # radians
spin1z = 0.0
spin2z = 0.0

# Generate frequency-domain waveform
hp, hc = get_fd_waveform(approximant="IMRPhenomD",
                         mass1=m1, mass2=m2,
                         spin1z=spin1z, spin2z=spin2z,
                         distance=distance,
                         inclination=inclination,
                         f_lower=20.0,
                         delta_f=1.0/64)

# Plot frequency domain
pylab.figure(0)
pylab.plot(hp.sample_frequencies, abs(hp))
pylab.xscale('log')
pylab.yscale('log')
pylab.xlim(20, 512)
pylab.xlabel('Frequency (Hz)')
pylab.ylabel('Strain amplitude')
pylab.title('GW250114-like waveform (frequency domain)')

# Convert to time domain
ht = hp.to_timeseries()

# Shift so that merger roughly at t=0
ht = ht.cyclic_time_shift(-ht.start_time)

# Plot time domain
pylab.figure(1)
pylab.plot(ht.sample_times, ht.real())
pylab.xlim(-0.2, 0.05)
pylab.xlabel('Time (s)')
pylab.ylabel('Strain')
pylab.title('GW250114-like waveform (time domain)')
pylab.show()
