2024-08-14 21:40

Status: #baby

Tags: [[wireless]] [[protocols]] [[radio communications]] [[data transmission]]

# Wi-FI

Wi-Fi was named by the Wireless Ethernet Compatibility Alliance ([[WECA]]) in an attempt to push the term "Wireless Fidelity" for the 802.11 [[IEEE]] Standard, also sometimes called *wireless ethernet*.  It was intended to be reminiscent of "high fidelity", a concept push towards consumers to inspire thoughts of high quality service.

#### But why?
Mobility and flexibility. With wireless telephony, users are empowered to travel beyond their point of contact, their call handled by the cell network and passed off between towers. Wireless networks seek to emulate this same power but on a smaller scale.  It is also interesting to note that Europe was far quicker to adopt this technology on a widespread scale.

Flexibility is important especially in the case of so-called "hot-spot" providers, that being namely businesses such as cafes, restaurants, and hotels. While now, in 2024, such services are expected and standard, it used to be a way to differentiate one business from another.  But the simple act of being able to offer access without needing to run expensive and time-consuming cable drops, as well as the specialized knowledge to secure things at layer 1 and layer 2 profoundly changed how we interact with information. 

Wireless networks also have the benefit of bringing network access to rural communities where running extensive wired infrastructure is too expensive for the return, offering a competitive experience for those users.

### Radio Spectrum as a Resource

The usage of the radio spectrum became hotly contested as the devices to transmit and receive information across it became more prevalent, thanks to the works of engineers such as Marconi and Tesla.  Licensing its usage especially proved to be a fruitful endeavor for many governments, offering specific frequency bands for special usage.

Each band has an associated bandwidth, which is simply how much frequency is available in that band. Generally, a higher frequency band correlates to more data being transmitted. This is why the 5 GHz band in Wi-Fi for example can transmit data much faster than the 2.4 GHz band, with the drawbacks of course that come with shorter wavelengths.

In the past, an analog mobile telephone signal might only need some 20 kHz, while a TV signal, carrying vastly more information (audio and video, luminance, chrominance, etc), might require 6 MHz.

In the US, such licensing is regulated by the [[FCC]], while abroad the [[ERO]] and [[ITU]] handle similar allocation.  It is also important to note that in the US, we have only 11 of 14 channels available while in Europe they can access 13, and in Japan they utilize all 14.

The ISM bands (Industrial, Scientific, Medicine) occupy several bands. This is because the equipment operating in these ranges are used for a variety of equipment that would be too cumbersome to maintain licensing records for.  Requiring a license to operate a microwave oven, for example, which operates in the same frequency band as an 802.11b device would be rather overkill.


### The Limits of Wireless Networking

Wireless networks aren't meant to replace wired networks, however.  More of an enhancement or extension.  Servers for instance don't need to be mobile (well, for the most part), so being wired makes sense, especially as wired connections don't suffer nearly as many issues with interference and complications involving propagation.  

Wireless connections also have a forced limit imposed upon them by the band they occupy, further reduced by activity and other actors within the band.  Wireless networks also require additional overhead when receiving frames to guard against loss from the medium.

Security is another concern, one far more complex than with wired connections, which naturally are safeguarded at the physical layer.  While it is possible for a bad actor to gain access to free ethernet ports, there are often equally simple ways to guard against such access (Discretionary MAC port access and the like, or simply turning off ports not in use).  A wireless transmission is designed so that anyone with the appropriate hardware can receive the transmission, so it is of course much more difficult to make certain that such a transmission cannot be easily scrutinized by anyone with a will and an antenna.

### A Network By Any Other Name

Wi-Fi was made popular due to price erosion from technological advancements primarily by Apple around 1999, as well as of course the aforementioned advantages it brings to the table.  Several standards were developed and improved upon from 1997-1999 that helped facilitate this shift in networking as well.

802.11a and 802.11b expanded upon Direct Sequence (DS) and Frequency Hopping (FH) with another mode called Orthogonal Frequency Division Multiplexing (OFDM). 802.11a and b provide faster speeds than 10Base-T and is competitive with Fast Ethernet.

![[Pasted image 20240814231923.png]]


### How Wi-Fi emulates Ethernet

At the core of 802.11 is the simple goal of remaining as similar to Ethernet as possible within the constraints of the wireless medium.  Wireless NICs even have the same 48-bit MAC address pools that Ethernet cards do.  This is so that, for the most part, devices treat these clients the same (outside of the network at least).  For the base stations within the LAN, they have a clear understanding that these devices are different, and most importantly, are *mobile*.

### The 802 Family

Wi-Fi is just part of the many specifications of the IEEE 802 standards developed for networking, particularly LAN.  These are focused on the two lowest layers of the [[OSI]] model, the Physical and the Data Link layers.  All 802 networks thus concern themselves with both a MAC and Physical component.  The secondary number in the specification is what identifies the standard.

802.3 for example is the specification for Carrier Sense Multiple Access with Collision Detection (CSMA/CD). 802.5 is Token Ring, 802.2 is the Logical Link Control, and 802.1 has many standards for management.  802.1d is bridging, for example, and VLANs are on 802.1q.

802.11 contains a few different technologies and can be considered just another link layer able to use the 802.2/LLC encapsulation.  It employs FHSS from the physical layer and the DSSS from the link layer.  802.11b added High-Rate DSSS.

### PHY Components

802.11 consists of two particular methods for emulating the physical medium onto the radio waves that transmit the data to the mobile clients.  The first is the Physical Layer Convergence Procedure (PLCP) which actually maps the data onto the frames, the second being the Physical Medium Dependent (PMD) system that actually transmits the frames.

## Reference:

[[802.11 Wireless Networks The Definitive Guide]]
