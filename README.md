# Sending notifications upon script completion--

## SMS message upon completion of Python script
This code utilizes the Twilio services to send a text message to one phone number once an execution has finished. This does require a Twilio account, but the Twilio free trial is sufficient if you only want to send messages to one number. The free trial does not technically expire; the service simply provides a prepaid limit of something like $15. Texts are very cheap, like less than 5 cents each, which means you can get away with the trial unless you plan on sending an inordinate amount oftexts to yourself, would like a phone call instead, or need to send texts to multiple numbers. 

Get started here: https://www.twilio.com/try-twilio

Once you have set up an account through Twilio, you will recieve a new phone number and a secret client ID. These are very important. 
Otherwise the code is very simple and adaptable. Mine sends text upon completion or sends a message when an error occurs. 

# Slack message upon completion of Stata .do files
I also forked a scrpt from peer in the BYU Economics Department and Record Linking Lab that sends a message to your Slack once a Stata .do file is finished. Below is both the accredidation and original text of the repository ReadMe. See Tommy's other work at https://gitgub.com/tmorg46/.

*Coming soon: Using Slack messaging SDK to send text or email for script notificatons via Python*

***
**Start Forked ReadMe**

## stata_sendtoslack

send yourself a direct message on Slack when a Stata do file starts, fails, and/or finishes
code written by others as credited in each file

instructions are listed in each file and below.

from the original readme.do file, written by Jared and modified for this repository:

/*
Jared Wright
jaredwright217@gmail.com
16 September 2021
sendtoslack is a program that allows you to send notifications to your phone via slack
I use it to notify me when a long do file has finished running or breaks as well as to notify me in the middle of do files.
To receive notifications on your phone, you will need to have slack installed on your phone. You will also need a private url. 
Feel free to email with any questions
*/

For more information on setting up sendtoslack, run the following commands:
```
ssc install sendtoslack
help sendtoslack
```
This is an example of how to use sendtoslack in a do file
```
capture program drop sendtoslack sts_Send sts_Saveurl
run "the path to the .ado file"
sleep 3000
sendtoslack, url("your url") message("Someone ran the readme.do file in the sendtoslack folder")
```
After creating your custom url, you can add a custom name to the sendtoslack.ado file. You can add a custom name in at around line 50 in the .ado file

Now you can send yourself notifications while a do file is running.

To receive a notification when the do file finishes or breaks, use the sendtoslack file. Just change the macros. Then instead of running your do file, run that file.

**End Forked ReadMe**

***
Tommy, Jared, and Collin are either current or alum undergraduate students at Brigham Young University. We ask that any redistribution or reference to publicized code be attributed with the author name and school affiliation, along with a hyperlink to this repository. 

Inquieries may be sent to Collin: zoellercollin@gmail.com https://github.com/ColZoel

