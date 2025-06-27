https://github.com/afoley587/flink-with-python


Build a kafka system from the external source (producer-consumer pair) to a source that talks to open-webui (producer-consumer pair). 

The first part to work on is authentication of the user. The kafka gets handled by flink which stores it in a flink file source. The sink file is then accessed in some way by the channels (in channels.py) when new data is inputted. Can use a watchdog to watch for inputs in sink file.

