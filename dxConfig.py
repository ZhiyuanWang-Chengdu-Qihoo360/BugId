import os;
sBaseFolderPath = os.path.dirname(__file__);
dxConfig = {
  "bSaveReport": True,                            # Set to True to have BugId.py output a HTML formatted crash report.
  "asSymbolServerURLs": [                         # List of symbol server URLs for use by cdb.
    "http://msdl.microsoft.com/download/symbols"
  ],
  "nExcessiveCPUUsageCheckInitialTimeout": 5,     # Start checking the application for excessive CPU usage after this
                                                  # many seconds. Lower values yield results faster, but slow down
                                                  # testing and may give false positives if startup takes long.
  "sTest": "http://%s:28876/" % os.getenv("COMPUTERNAME"), # Default URL for browser tests, can be a file path for
                                                  # applications that read test data from a file.
  "nApplicationMaxRunTime": None,                 # Terminate BugId if the application has been running for this many
                                                  # seconds without crashing. None to allow the application to run
                                                  # forever.
  "bShowLincenseAndDonationInfo": True,           # Set to False to disable the licensing and donations information
                                                  # shown at the end of each run. Feel free to act on it first :)
  "BugId": {
    # The values from src\dxBugIdConfig.py get loaded here, but you can override them here.
  },
};