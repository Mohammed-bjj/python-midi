#!/home/mohammed/anaconda3/envs/ganRNN/bin/python
"""
Print a description of the available devices.
"""
import midi.sequencer as sequencer

s = sequencer.SequencerHardware()

print s
