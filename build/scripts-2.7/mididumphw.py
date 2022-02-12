#!/home/mohammed/anaconda3/envs/env3/bin/python
"""
Print a description of the available devices.
"""
import midi.sequencer as sequencer

s = sequencer.SequencerHardware()

print s
