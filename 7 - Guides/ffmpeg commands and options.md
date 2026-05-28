
Tags: [[video-conversion]], [[graphics programming]] [[media encoding]]

# Setting up FFMPEG on Windows

1. Download from https://ffmpeg.org/download.html.
2. Click the big ass Windows button
3. Either download repo works, doesn't really matter
4. Extract here etc.
5. Press Windows key
6. Type in "System Path". It should show something like
   ![[Pasted image 20240917144726.png]]
7. Click that.
8. Click "Environment Variables" 
![[Pasted image 20240919082630.png]]
10. Double click the PATH variable under the System variables section
11. ![[Pasted image 20240919083046.png]]
12. Hit New
13. Copy in the path for the FFMPEG installation (aka the directory you extracted it to)
14. Open up a command prompt
15. Type ffmpeg -version to check if it's configured correctly.

## Commands

`ffpmeg -version`

Shows current version and just a good way to check if it's properly configured in the System PATH.

## General syntax for conversion

`ffmpeg -i input.mp4 <conversion option flags> output.x`

Some sample options

`-r` allows for targeting the output frame rate. Has a pretty big impact of performance/file size. Just type the fps number itself

-vf is the filter chain tag. As of now, we know of using it to target the scale and some peripheral options, such as fps.

**Example**

`ffmpeg -i input.mp4 -vf "fps=20, scale=500:-1" output.webp`

the `-1` portion of the filter chain tells ffmpeg to keep the aspect ratio equivalent.

## Clipping
`-ss` allows for clipping.  use the epoch of `00:00:00` to define the start of the clip, then `-t` for the duration. 

## Encoding 

`-c` will allow for copying the video/audio directly without re-encoding. This is faster and results in lossless production.

`"scale=iw:ih"` can be used to scale the conversion to its original dimensions (iw = width and ih = height, shocker). Apparently it's pretty redundant, but a good failsafe.

`-compression_level 0` sets the PNG compression level to the highest quality (lowest compression).  Scale goes from 0 to 9 (typical bit range).

a good conversion for mp4->webp is

`ffmpeg -i input.mp4 -vf "scale=1280:720, fps=25" -loop 0 output.webp`

## Looping

`-loop 0` makes an animated image format like webp actually continuously loop. Without this, it will only play a single time per load.


# Stitching videos together

Easiest way is to use the concatenation demuxer.

Make a text file in the same directory as the videos named inputs.txt (doesn't matter just convention), with the lines

```
file 'video1.mp4'
file 'video2.mp4'
```

Then run this command

`ffmpeg -f concat -safe 0 -i inputs.txt -c copy output.mp4`
