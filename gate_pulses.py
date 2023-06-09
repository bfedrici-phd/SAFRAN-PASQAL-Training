# -*- coding: utf-8 -*-
"""gate_pulses.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HLhXBVVBZ33Dn4_yIR_tvh3Ucu6sQc68
"""

from pulser import Pulse
from pulser.waveforms import BlackmanWaveform
import numpy as np

def u3_pulse(gamma_angle, theta_angle, phi_angle, pulse_duration=1000):
  custom_wf = BlackmanWaveform(pulse_duration, theta_angle)
  u3_pulse = Pulse.ConstantDetuning(
      amplitude=custom_wf, detuning=0, phase=phi_angle, post_phase_shift=phi_angle + gamma_angle
      )
  return u3_pulse

def x_pulse(pulse_duration=1000):
  pi_wf = BlackmanWaveform(pulse_duration, np.pi)
  x_pulse = Pulse.ConstantDetuning(
      pi_wf, detuning=0, phase=np.pi / 2, post_phase_shift=np.pi
      )
  return x_pulse

def y_pulse(pulse_duration=1000):
  pi_wf = BlackmanWaveform(pulse_duration, np.pi)
  y_pulse = Pulse.ConstantDetuning(
      pi_wf, detuning=0, phase=0, post_phase_shift=np.pi
      )
  return y_pulse

def h_pulse(pulse_duration=1000):
  half_pi_wf = BlackmanWaveform(pulse_duration, np.pi / 2)
  h_pulse = Pulse.ConstantDetuning(
      amplitude=half_pi_wf, detuning=0, phase=np.pi / 2, post_phase_shift=np.pi
      )
  return h_pulse

def rx_pulse(rot_angle, pulse_duration=1000):
  rot_angle_wf = BlackmanWaveform(pulse_duration, rot_angle)
  rx_pulse = Pulse.ConstantDetuning(
      rot_angle_wf, detuning=0, phase=0, post_phase_shift=0
      )
  return rx_pulse

def rx_dag_pulse(rot_angle, pulse_duration=1000):
  rot_angle_wf = BlackmanWaveform(pulse_duration, rot_angle)
  rx_dag_pulse = Pulse.ConstantDetuning(
      rot_angle_wf, detuning=0, phase=np.pi, post_phase_shift=0
      )
  return rx_dag_pulse

def ry_pulse(rot_angle, pulse_duration=1000):
  rot_angle_wf = BlackmanWaveform(pulse_duration, rot_angle)
  ry_pulse = Pulse.ConstantDetuning(
      rot_angle_wf, detuning=0, phase=-np.pi / 2, post_phase_shift=0
      )
  return ry_pulse

def ry_dag_pulse(rot_angle, pulse_duration=1000):
  rot_angle_wf = BlackmanWaveform(pulse_duration, rot_angle)
  ry_dag_pulse = Pulse.ConstantDetuning(
      rot_angle_wf, detuning=0, phase=np.pi / 2, post_phase_shift=0
      )
  return ry_dag_pulse
