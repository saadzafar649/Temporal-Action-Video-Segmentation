# -*- coding: utf-8 -*-
"""I3D Feature Extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LKoytZmNxtC-EuCp7pHDM6sFvK1XdwlW

<figure>
  <img src="https://github.com/v-iashin/video_features/raw/master/docs/_assets/i3d.png" width="300" />
</figure>

The `video_features` library allows you to extract features from
raw videos in parallel with multiple GPUs.
It supports several extractors that capture visual appearance,
optical flow, and audio features. See more details in the
[GitHub repository](https://github.com/v-iashin/video_features).

See more feature extraction examples in colaboratory notebooks:
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Zd7r8uKGLGSxlil4PPnXk_4I3KOsjPpO?usp=sharing) – CLIP
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1HUlYcOJf_dArOcAaR9jaQHuM5CAZiNZc?usp=sharing) – S3D
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1LKoytZmNxtC-EuCp7pHDM6sFvK1XdwlW?usp=sharing) – I3D
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1csJgkVQ3E2qOyVlcOM-ACHGgPBBKwE2Y?usp=sharing) – R(2+1)D
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18I95Rn1B3a2ISfD9b-o4o93m3XuHbcIY?usp=sharing) – RAFT
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/17VLdf4abQT2eoMjc6ziJ9UaRaOklTlP0?usp=sharing) – ResNet
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1r_8OnmwXKwmH0n4RxBfuICVBgpbJt_Fs?usp=sharing) – VGGish
"""

! git clone https://github.com/v-iashin/video_features.git
! pip install omegaconf==2.0.6

# Commented out IPython magic to ensure Python compatibility.
# %cd video_features

from models.i3d.extract_i3d import ExtractI3D
from utils.utils import build_cfg_path
from omegaconf import OmegaConf
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.cuda.get_device_name(0)

# Select the feature type
feature_type = 'i3d'

# Load and patch the config
args = OmegaConf.load(build_cfg_path(feature_type))
args.video_paths = ['./sample/v_GGSY1Qvo990.mp4']
# args.show_pred = True
# args.stack_size = 24
# args.step_size = 24
# args.extraction_fps = 25
args.flow_type = 'raft' # 'pwc' is not supported on Google Colab (cupy version mismatch)
# args.streams = 'flow'

# Load the model
extractor = ExtractI3D(args)

# Extract features
for video_path in args.video_paths:
    print(f'Extracting for {video_path}')
    feature_dict = extractor.extract(video_path)
    [(print(k), print(v.shape), print(v)) for k, v in feature_dict.items()]

! pip freeze