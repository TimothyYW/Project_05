#!/bin/bash
# Script to allow Heroku API key to be pasted
# exported as an environment variable
#
# Matt Rudge, May 2021

echo "Heroku authentication configuration script"
echo "Code Institute, 2021"
echo
echo "Get your Heroku API key by going to https://dashboard.heroku.com"
echo "Go to Account Settings and click on Reveal to view your Heroku API key"
echo

if [[ -z "${HEROKU_API_KEY}" ]]; then
   echo "Paste your Heroku API key here or press Enter to quit:"
   read apikey
   if [[ -z "${apikey}" ]]; then
      exit 0  # Exit the script if no API key is provided
   fi
   # Check if the API key is already in .bashrc
   if grep -q "export HEROKU_API_KEY=" ~/.bashrc; then
      echo "API key already exists in .bashrc. Skipping addition."
   else
      echo "export HEROKU_API_KEY=${apikey}" >> ~/.bashrc
      echo "Added the export. Refreshing the terminal."
      . ~/.bashrc > /dev/null
      echo "Done!"
   fi
else
   echo "API key is already set."
   echo
   echo "To reset the API key, please input 'reset':"
   read reset_trigger
   if [[ ${reset_trigger} == "reset" ]]; then
      unset HEROKU_API_KEY
      # Remove the line containing the HEROKU_API_KEY from .bashrc
      sed -i '/export HEROKU_API_KEY=/d' ~/.bashrc
      echo
      echo "API key removed!"
   else
      unset reset_trigger
      echo "API key unchanged."
   fi
   echo
   echo "Exiting"
fi
xiting
fi
