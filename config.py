import sys
sys.path.append('/home/zhouyj/software/PAD')
import data_pipelines as dps
import pickers

class Config(object):
  def __init__(self):

    # Template cut
    self.win_len  = 45       # cut window length
    self.t_blank  = 15       # time before P in the cut window
    self.min_sta  = 4        # min sta num for a template events
    self.chn_dict = {'ZSY':['HHE','HHN','HHZ'], 
                     'YN': ['HHE','HHN','HHZ'],
                     'XLS':['HHE','HHN','HHZ']}
    self.get_data_dict = dps.Data(None).get_data_dict

    # MFT params
    self.temp_win_trig = [1., 9.] # win fr trig temp cut, rel p
    self.temp_win_p = [0.5, 1.5]   # win for p temp cut, rel p 
    self.temp_win_s = [0.5, 1.5]     # win for s temp cut, rel s
    self.trig_thres = 0.25        # cc thres for det & mask
    self.mask_len = 1.            # win len for cc mask
    self.det_gap = 5.             # gap sec for detection
    self.ppk_win_p = [1., 1.]     # win for p pick
    self.ppk_win_s = [2., 2.]     # win for s pick
    self.amp_win = [0, 6]         # win for amplitude measurement

    # data process
    self.resp_dict = {'ZSY': 3.02e8,
                      'YN': 1.67785e9,
                      'XLS': 1/1.6e-9}  # instrumental gain (cnt/m/s)
    self.samp_rate = 50
    self.freq_band = ['bandpass', [1., 40.]]
    self.picker = pickers.Trad_PS(samp_rate=self.samp_rate)
    self.num_workers = 5
