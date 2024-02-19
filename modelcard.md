---
# MODEL CARD

# Model Card for Autism Emotion Detection Model

Bu model, otizm spektrum bozukluğu tanısı konmuş bireylerin duygusal ifadelerini anlamalarına yardımcı olmak için geliştirilmiştir. Model, Fer2013 veri seti üzerinde eğitilmiş ve otizm spektrum bozukluğu tanısı konmuş bireylerin diğer insanların duygusal ifadelerini anlamalarını kolaylaştırmak amacıyla kullanılabilir.

## Model Details

### Model Description

Bu model, derin öğrenme tekniklerini kullanarak duygusal ifadeleri tanımak ve yorumlamak için eğitilmiştir. Otizm spektrum bozukluğu tanısı konmuş bireylerin duygusal ifadeleri anlamalarına yardımcı olmak için tasarlanmıştır.

{{ model_description | default("", true) }}

- **Developed by:** Elif Özbay
- **Model date:** 
- **Model type:** Derin Öğrenme (Convolutional Neural Network)
- **Language(s):** Python
- **Finetuned from model [optional]:** {{ base_model | default("[More Information Needed]", true)}}

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/iremgulcin/Elif-Ozbay/tree/master
- **Paper [optional]:** 
- **Demo [optional]:** 

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

{{ direct_use | default("[More Information Needed]", true)}}


### Out-of-Scope Use

Bu model, genel duygu tanıma veya teşhisler için kullanılmak üzere tasarlanmamıştır.

## Bias, Risks, and Limitations

Bu modelin doğruluğu %55 civarındadır, bu nedenle her zaman doğru tahminler yapmayabilir. Ayrıca, modelin iğrenmiş duygusunu tahmin etme yeteneği sınırlı olabilir ve korku ile şaşkınlığı karıştırabilir.

### Recommendations

Kullanıcılar (hem doğrudan hem de downstream) modelin risklerini, önyargılarını ve sınırlamalarını bilinçli bir şekilde anlamalıdır. Modelin kullanımı sırasında dikkatli olunmalı ve sonuçların profesyonel bir danışmandan alınan tavsiyelerle yorumlanması önerilir.

## How to Get Started with the Model

Modeli kullanmaya başlamak için aşağıdaki kodu kullanabilirsiniz:

python main.py

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

Model, Fer2013 veri seti üzerinde eğitilmiştir. Bu veri seti, çeşitli duygusal ifadeler içeren yüz ifadelerini içermektedir.

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->
Model, evrişimli sinir ağı (CNN) mimarisi kullanılarak eğitilmiştir. Eğitim sürecinde, veri seti ön işleme adımlarından geçirilmiş ve belirli hiperparametreler kullanılarak model eğitilmiştir.

#### Preprocessing [optional]

{{ preprocessing | default("[More Information Needed]", true)}}


#### Training Hyperparameters

- **Training regime:** {{ training_regime | default("[More Information Needed]", true)}} <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

{{ speeds_sizes_times | default("[More Information Needed]", true)}}

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

Test verisi, Fer2013 veri seti üzerinde ayrılmış bir test setinden seçilmiştir.

#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

{{ testing_factors | default("[More Information Needed]", true)}}

#### Metrics

Modelin performansı, doğruluk (accuracy) ve kayıp (loss) metrikleri kullanılarak değerlendirilmiştir.

### Results

{{ results | default("[More Information Needed]", true)}}

#### Summary

{{ results_summary | default("", true) }}

## Model Examination [optional]

<!-- Relevant interpretability work for the model goes here -->

{{ model_examination | default("[More Information Needed]", true)}}


## Technical Specifications [optional]

### Model Architecture and Objective

{{ model_specs | default("[More Information Needed]", true)}}

### Compute Infrastructure

{{ compute_infrastructure | default("[More Information Needed]", true)}}

#### Hardware

{{ hardware_requirements | default("[More Information Needed]", true)}}

#### Software

{{ software | default("[More Information Needed]", true)}}






