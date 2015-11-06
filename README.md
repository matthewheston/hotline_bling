## Hotline Bling ##

**Who do you text late night?**

If you use iMessage and back up your message on your Mac, now you can find out!
This script will connect to your iMessage database and search for people you
text between midnight and three AM.

## Instructions ##

Rename `constants.py.examples` to `constants.py`. The default path to iMessage
should be fine, but if you happen to know yours is different, you can change it
here. Change `days` to be an array of the weekdays you want to include in the
search. (Remember this searches for midnight to 3AM. So if you're interested in
late Friday night and late Saturday night, the array should include `SATURDAY`
and `SUNDAY`.) Right now the script will only search within one calendar year,
but you can modify which year by setting the `year` variable here.

Then just run `python hotline_bling.py`. It will print out an ordered list of
all people you have texted during the time period as well as a count of how many
texts you sent them.
