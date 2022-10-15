from twilio.rest import Client


def send(csv_dir=None, filename=None,
         flagged_file=None,
         from_= '<your Twilio-assigned phone# >', to='<your personal phone # >',
         error=False, is_file=False, flagged=False):
    
    c = Client('[Account_SID]',
               '[AuthToken]')  # Replace with your own information 
    if is_file:
        message = c.messages.create(
            body='There was a problem with {}'.format(filename),
            to=to,
            from_=from_)
    elif error:
        message = c.messages.create(
            body='There was a problem with the script.',
            to=to,
            from_=from_)
    elif flagged:
        message = c.messages.create(
            body='the CSV {} found several flagged items. You should take a look'.format(flagged_file),
            to=to,
            from_=from_)
    else:
        message = c.messages.create(
            body='Success! Python script was executed successfully.',
            to=to,
            from_=from_)


# you can wrap this with a <Try> function that will then define what to do when an error occurs. Remember this is just a skeleton. 
