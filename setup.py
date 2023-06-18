from setuptools import setup, find_packages
from functools import reduce

version="0.0.0"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='phishintention',
      version="0.0.0",
      description='phishintention',
      long_description=long_description,
      author='Ruofan Liu',
      author_email='liu.ruofan16@u.nus.edu',
      url='https://github.com/lindsey98/PhishIntention',
      license='Apache License 2.0',
      python_requires='==3.8.*',
      packages=['phishintention', 'phishintention.src',

                'phishintention.src.AWL_detector_utils',
                'phishintention.src.AWL_detector_utils.configs',
                'phishintention.src.AWL_detector_utils.configs.bases',
                'phishintention.src.AWL_detector_utils.detectron2_1',
                'phishintention.src.AWL_detector_utils.detectron2_1.configs',
                'phishintention.src.AWL_detector_utils.detectron2_1.modelling',

                'phishintention.src.crp_classifier_utils',
                'phishintention.src.crp_classifier_utils.bit_pytorch',
                'phishintention.src.crp_classifier_utils.HTML_heuristic',
                'phishintention.src.crp_classifier_utils.output',
   
                'phishintention.src.crp_locator_utils',
                'phishintention.src.crp_locator_utils.login_finder',
                'phishintention.src.crp_locator_utils.login_finder.configs',
                'phishintention.src.crp_locator_utils.login_finder.configs.bases',
                'phishintention.src.crp_locator_utils.login_finder.detectron2_1',
                'phishintention.src.crp_locator_utils.login_finder.detectron2_1.configs',
                'phishintention.src.crp_locator_utils.login_finder.detectron2_1.modelling',
           
                'phishintention.src.OCR_siamese_utils',
                'phishintention.src.OCR_siamese_utils.lib',
                'phishintention.src.OCR_siamese_utils.lib.datasets',
                'phishintention.src.OCR_siamese_utils.lib.evaluation_metrics',
                'phishintention.src.OCR_siamese_utils.lib.loss',
                'phishintention.src.OCR_siamese_utils.lib.models',
                'phishintention.src.OCR_siamese_utils.lib.tools',
                'phishintention.src.OCR_siamese_utils.lib.utils',
                'phishintention.src.OCR_siamese_utils.output',
               
                'phishintention.src.OCR_siamese_utils.siamese_unified',
                'phishintention.src.OCR_siamese_utils.siamese_unified.bit_pytorch',
                'phishintention.src.phishpedia_siamese.siamese_retrain',
                'phishintention.src.phishpedia_siamese.siamese_retrain.bit_pytorch',
                'phishintention.src.util',
                'phishintention.src.phishpedia_siamese',
                ],
      install_requires=[
          'torchsummary',
          'scipy',
          'tldextract',
          'opencv-python',
          'selenium',
          'helium',
          'selenium-wire',
          'webdriver-manager',
          'pandas',
          'numpy',
          'tqdm',
          'Pillow',
          'pathlib',
          'fvcore',
          'pycocotools',
          'scikit-learn',
          'pyyaml',
          'cryptography==38.0.4',
          'typing_extensions',
          'gspread',
          'oauth2client',
          'lxml',
          # 'selenium==3.141.0',
          'helium',
          'h2',
          'hyperframe',
          'fuzzywuzzy',
          'h11==0.8.1',
      ],
      package_data={
            # If any package contains *.txt or *.rst files, include them:
            "": ["*.yaml", "*.txt", "*.exe"],
      },
      include_package_data=True
      )
