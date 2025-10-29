# RaSound
Random sound interval app

Format for settings_file.txt is:

File Location   Percent chance  Time
TestSounds\jumpscare.mp3 .20 second
TestSounds\disconnect.mp3 .50 minute
TestSounds\cave-sound.mp3 1 hour

So disconnect.mp3 will have a 50/50 chance of playing every minute while
jumpscare.mp3 will only have a 20% chance of playing every second.

Cave-sound.mp3 has a high chance of playing at least once per hour

The settings_file.txt can have multiple of these settings but have them in the same format as stated above