Tags: [[Weakauras]], [[WoW API]]

The simplest way is to set up the triggers as normal. For example:

Make a Weakaura that triggers on cast start, such as for a boss mechanic, or for an upcoming boss ability by hooking in to the boss timers of BigWigs.

Then, go to Actions. At the bottom of Actions, you should see "Run Custom Code".

![[Customcodeweakaura.png]]

Click on that, and a field to enter in custom scripts should open. You don't need to tell Weakauras to "run" the script. You can just enter in whatever script you want as is.

So, for this, the CVar to run TTS is:

`C_VoiceChat.SpeakText(voiceID, text, destination, rate, volume);`

Where text should be a string, as in encapsulated within quotes.

**Destination should generally be, " Enum.VoiceTtsDestination.LocalPlayback"**

Rate is a value in the range 0-10 for faster speech, while 0-(-10) is slower speech.

Volume is self explanatory.

You can test what the TTS should sound like by just running this with `/run` prepended to it.

So,

`/run C_VoiceChat.SpeakText(0, "Check Markers", Enum.VoiceTtsDestination.LocalPlayback, 0, 100)`
for example.

![[CheckMarkers.png]]