%define debug_package %{nil}

Name     : caffe
Version  : 0.1rc3
Release  : 1
URL      : https://github.com/BVLC/caffe
Source0  : caffe-0.1rc3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: caffe-bin
Requires: caffe-python
Requires: caffe-lib
Requires: caffe-data
BuildRequires : boost-devel
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : gflags-devel
BuildRequires : glog-devel
BuildRequires : python2-h5py
BuildRequires : hdf5-devel
BuildRequires : leveldb-devel
BuildRequires : lmdb-devel
BuildRequires : python-nose
BuildRequires : python2-numpy
BuildRequires : openblas-devel
BuildRequires : opencv-devel
BuildRequires : protobuf-devel
BuildRequires : python-devel
BuildRequires : python2-scipy
BuildRequires : snappy-devel
#Patch1: config.patch
#Patch2: 0001-add-InputLayer-for-Net-input.patch
#Patch3: 0002-deprecate-input-fields-and-upgrade-automagically.patch
#Patch4: 0003-drop-Net-inputs-Forward-with-bottoms.patch
#Patch5: 0004-collect-Net-inputs-from-Input-layers.patch
#Patch6: 0005-examples-switch-examples-models-to-Input-layers.patch
#Patch7: 0006-Deprecate-ForwardPrefilled-Forward-bottom-loss-in-li.patch
#Patch8: faster-vector.patch
#Patch9: vector.patch
#Patch10: pow.patch

%description
Caffe is a deep learning framework made with expression, speed, and modularity in mind. It is developed by the Berkeley Vision and Learning Center (BVLC) and by community contributors. Yangqing Jia created the project during his PhD at UC Berkeley.

%package bin
Summary: bin components for the caffe package.
Group: Binaries
Requires: caffe-data

%description bin
bin components for the caffe package.


%package data
Summary: data components for the caffe package.
Group: Data

%description data
data components for the caffe package.


%package devel
Summary: devel components for the caffe package.
Group: Development
Requires: caffe-lib
Requires: caffe-bin
Requires: caffe-data
Provides: caffe-devel

%description devel
devel components for the caffe package.


%package lib
Summary: lib components for the caffe package.
Group: Libraries
Requires: caffe-data

%description lib
lib components for the caffe package.


%package python
Summary: python components for the caffe package.
Group: Default

%description python
python components for the caffe package.


%prep
%setup -q -n %{name}-%{version}
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1
#%patch5 -p1
#%patch6 -p1
#%patch7 -p1
#%patch8 -p1
#%patch9 -p1
#%patch10 -p1

%build
export LANG=C
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DUSE_LEVELDB=on -DUSE_OPENCV=on  -DBLAS=open
make VERBOSE=1  %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
## make_install_append content
mkdir -p %{buildroot}/%{_libdir}
mv %{buildroot}/usr/lib/lib*so* %{buildroot}/%{_libdir}
rm -rf %{buildroot}/usr/lib/libproto.a
mkdir -p %{buildroot}/%{_libdir}/python2.7/site-packages/
mv %{buildroot}/usr/python/* %{buildroot}/%{_libdir}/python2.7/site-packages/
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%{_bindir}/caffe
%{_bindir}/classification
%{_bindir}/compute_image_mean
%{_bindir}/convert_cifar_data
%{_bindir}/convert_imageset
%{_bindir}/convert_mnist_data
%{_bindir}/convert_mnist_siamese_data
%{_bindir}/device_query
%{_bindir}/extract_features
%{_bindir}/finetune_net
%{_bindir}/net_speed_benchmark
%{_bindir}/test_net
%{_bindir}/train_net
%{_bindir}/upgrade_net_proto_binary
%{_bindir}/upgrade_net_proto_text
%{_bindir}/upgrade_solver_proto_text

%files data
%defattr(-,root,root,-)
/usr/share/Caffe/CaffeConfig.cmake
/usr/share/Caffe/CaffeTargets-release.cmake
/usr/share/Caffe/CaffeTargets.cmake

%files devel
%defattr(-,root,root,-)
/usr/include/caffe/blob.hpp
/usr/include/caffe/caffe.hpp
/usr/include/caffe/common.hpp
/usr/include/caffe/data_reader.hpp
/usr/include/caffe/data_transformer.hpp
/usr/include/caffe/filler.hpp
/usr/include/caffe/internal_thread.hpp
/usr/include/caffe/layer.hpp
/usr/include/caffe/layer_factory.hpp
/usr/include/caffe/layers/absval_layer.hpp
/usr/include/caffe/layers/accuracy_layer.hpp
/usr/include/caffe/layers/argmax_layer.hpp
/usr/include/caffe/layers/base_conv_layer.hpp
/usr/include/caffe/layers/base_data_layer.hpp
/usr/include/caffe/layers/batch_norm_layer.hpp
/usr/include/caffe/layers/batch_reindex_layer.hpp
/usr/include/caffe/layers/bias_layer.hpp
/usr/include/caffe/layers/bnll_layer.hpp
/usr/include/caffe/layers/concat_layer.hpp
/usr/include/caffe/layers/contrastive_loss_layer.hpp
/usr/include/caffe/layers/conv_layer.hpp
/usr/include/caffe/layers/cudnn_conv_layer.hpp
/usr/include/caffe/layers/cudnn_lcn_layer.hpp
/usr/include/caffe/layers/cudnn_lrn_layer.hpp
/usr/include/caffe/layers/cudnn_pooling_layer.hpp
/usr/include/caffe/layers/cudnn_relu_layer.hpp
/usr/include/caffe/layers/cudnn_sigmoid_layer.hpp
/usr/include/caffe/layers/cudnn_softmax_layer.hpp
/usr/include/caffe/layers/cudnn_tanh_layer.hpp
/usr/include/caffe/layers/data_layer.hpp
/usr/include/caffe/layers/deconv_layer.hpp
/usr/include/caffe/layers/dropout_layer.hpp
/usr/include/caffe/layers/dummy_data_layer.hpp
/usr/include/caffe/layers/eltwise_layer.hpp
/usr/include/caffe/layers/elu_layer.hpp
/usr/include/caffe/layers/embed_layer.hpp
/usr/include/caffe/layers/euclidean_loss_layer.hpp
/usr/include/caffe/layers/exp_layer.hpp
/usr/include/caffe/layers/filter_layer.hpp
/usr/include/caffe/layers/flatten_layer.hpp
/usr/include/caffe/layers/hdf5_data_layer.hpp
/usr/include/caffe/layers/hdf5_output_layer.hpp
/usr/include/caffe/layers/hinge_loss_layer.hpp
/usr/include/caffe/layers/im2col_layer.hpp
/usr/include/caffe/layers/image_data_layer.hpp
/usr/include/caffe/layers/infogain_loss_layer.hpp
/usr/include/caffe/layers/inner_product_layer.hpp
#/usr/include/caffe/layers/input_layer.hpp
/usr/include/caffe/layers/log_layer.hpp
/usr/include/caffe/layers/loss_layer.hpp
/usr/include/caffe/layers/lrn_layer.hpp
/usr/include/caffe/layers/memory_data_layer.hpp
/usr/include/caffe/layers/multinomial_logistic_loss_layer.hpp
/usr/include/caffe/layers/mvn_layer.hpp
/usr/include/caffe/layers/neuron_layer.hpp
/usr/include/caffe/layers/pooling_layer.hpp
/usr/include/caffe/layers/power_layer.hpp
/usr/include/caffe/layers/prelu_layer.hpp
/usr/include/caffe/layers/python_layer.hpp
/usr/include/caffe/layers/reduction_layer.hpp
/usr/include/caffe/layers/relu_layer.hpp
/usr/include/caffe/layers/reshape_layer.hpp
/usr/include/caffe/layers/scale_layer.hpp
/usr/include/caffe/layers/sigmoid_cross_entropy_loss_layer.hpp
/usr/include/caffe/layers/sigmoid_layer.hpp
/usr/include/caffe/layers/silence_layer.hpp
/usr/include/caffe/layers/slice_layer.hpp
/usr/include/caffe/layers/softmax_layer.hpp
/usr/include/caffe/layers/softmax_loss_layer.hpp
/usr/include/caffe/layers/split_layer.hpp
/usr/include/caffe/layers/spp_layer.hpp
/usr/include/caffe/layers/tanh_layer.hpp
/usr/include/caffe/layers/threshold_layer.hpp
/usr/include/caffe/layers/tile_layer.hpp
/usr/include/caffe/layers/window_data_layer.hpp
/usr/include/caffe/net.hpp
/usr/include/caffe/parallel.hpp
/usr/include/caffe/proto/caffe.pb.h
/usr/include/caffe/sgd_solvers.hpp
/usr/include/caffe/solver.hpp
/usr/include/caffe/solver_factory.hpp
/usr/include/caffe/syncedmem.hpp
/usr/include/caffe/test/test_caffe_main.hpp
/usr/include/caffe/test/test_gradient_check_util.hpp
/usr/include/caffe/util/benchmark.hpp
/usr/include/caffe/util/blocking_queue.hpp
/usr/include/caffe/util/cudnn.hpp
/usr/include/caffe/util/db.hpp
/usr/include/caffe/util/db_leveldb.hpp
/usr/include/caffe/util/db_lmdb.hpp
/usr/include/caffe/util/device_alternate.hpp
/usr/include/caffe/util/format.hpp
/usr/include/caffe/util/gpu_util.cuh
/usr/include/caffe/util/hdf5.hpp
/usr/include/caffe/util/im2col.hpp
/usr/include/caffe/util/insert_splits.hpp
/usr/include/caffe/util/io.hpp
/usr/include/caffe/util/math_functions.hpp
/usr/include/caffe/util/mkl_alternate.hpp
/usr/include/caffe/util/rng.hpp
/usr/include/caffe/util/signal_handler.h
/usr/include/caffe/util/upgrade_proto.hpp
%{_libdir}/*.so

%files lib
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files python
%defattr(-,root,root,-)
%{_libdir}/python*/*
