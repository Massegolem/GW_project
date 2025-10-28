import pylab
from pycbc.waveform import get_td_waveform
from scipy.ndimage import gaussian_filter1d
from scipy.signal import butter, filtfilt

# GW250114-like parameters
m1 = 100      # solar masses
m2 = 120     # solar masses
distance = 403  # Mpc
inclination = 0.0  # radians


# Generate time-domain waveform
hp, hc = get_td_waveform(approximant='IMRPhenomD',
                         mass1=m1, mass2=m2,
                         distance=distance,
                         inclination=inclination,
                         f_lower=20.0,
                         delta_t=1.0/4096)



## Plot time-domain strain
#pylab.figure(1)
#pylab.plot(hp.sample_times, hp, label='Original')
#pylab.xlim(-0.35, 0.15)
#pylab.xlabel('Time (s)')
#pylab.ylabel('Strain')
#pylab.title('GW250114-like waveform (time domain)')
#pylab.show()

# Create figure
pylab.figure(figsize=(15, 3))

# Plot the waveform
pylab.plot(hp.sample_times, hp, color='#fcbc58', linewidth=4)

# Remove all axis elements
pylab.axis('off')
pylab.xlim(-0.35, 0.15)

# Remove borders/margins
pylab.margins(0)
pylab.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Save as PNG with transparent background
pylab.savefig("waveform23.png", dpi=600, transparent=True)

# (Optional: show preview)
pylab.show()
