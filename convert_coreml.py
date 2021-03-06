import coremltools

# Convert a caffe model to a classifier in Core ML
coreml_model = coremltools.converters.caffe.convert(('caffe_model/snapshot_iter_20.caffemodel',
													 'caffe_model/deploy.prototxt',
													 'caffe_model/mean.binaryproto'),
													  image_input_names = 'data',
													  class_labels = 'caffe_model/labels.txt',
													  is_bgr=True, image_scale=255.)

# Now save the model
coreml_model.author = "Sanket Firodiya"
coreml_model.save('CatsDogs.mlmodel')