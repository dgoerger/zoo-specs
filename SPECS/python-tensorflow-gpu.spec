# Created by pyp2rpm-3.1.3
%global pypi_name tensorflow

Name:           python-%{pypi_name}-gpu
Version:        0.12.0rc1
Release:        1%{?dist}
Summary:        TensorFlow helps the tensors flow

License:        Apache 2.0
URL:            http://tensorflow.org/
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}_gpu-%{version}-cp27-none-linux_x86_64.whl
Source1:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}_gpu-%{version}-cp35-cp35m-linux_x86_64.whl
BuildArch:      x86_64
 
BuildRequires:  python-setuptools
BuildRequires:  python-six >= 1.10.0
BuildRequires:  python2-devel
BuildRequires:  python-mock >= 2.0.0
BuildRequires:  python-numpy >= 1.11.0
BuildRequires:  python-protobuf == 3.0.0
BuildRequires:  python-scipy >= 0.15.1
BuildRequires:  python-wheel
BuildRequires:  python-pip

BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-devel
BuildRequires:  python3-mock >= 2.0.0
BuildRequires:  python3-numpy >= 1.11.0
BuildRequires:  python3-protobuf == 3.0.0
BuildRequires:  python3-scipy >= 0.15.1
BuildRequires:  python3-wheel
BuildRequires:  python3-pip

%description
TensorFlow is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) that flow between them. This flexible architecture lets you deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device without rewriting code. TensorFlow also includes TensorBoard, a data visualization toolkit.

%package -n     python2-%{pypi_name}-gpu
Summary:        TensorFlow helps the tensors flow
%{?python_provide:%python_provide python2-%{pypi_name}-gpu}
 
Requires:       python-six >= 1.10.0
Requires:       python-mock >= 2.0.0
Requires:       python-numpy >= 1.11.0
Requires:       python-protobuf == 3.0.0
Requires:       python-wheel
# assumes http://negativo17.org/nvidia-driver/
Requires:       cuda-devel => 8.0
Requires:       cuda-cudnn-devel => 5.0
# can't have both GPU and CPU-only versions installed simultaneously
Conflicts:      python2-tensorflow
%description -n python2-%{pypi_name}-gpu
tensorflow-gpu for python2 (CUDA)

%package -n     python3-%{pypi_name}-gpu
Summary:        TensorFlow helps the tensors flow
%{?python_provide:%python_provide python3-%{pypi_name}-gpu}
 
Requires:       python3-six >= 1.10.0
Requires:       python3-mock >= 2.0.0
Requires:       python3-numpy >= 1.11.0
Requires:       python3-protobuf == 3.0.0
Requires:       python3-wheel
# assumes http://negativo17.org/nvidia-driver/
Requires:       cuda-devel => 8.0
Requires:       cuda-cudnn-devel => 5.0
# can't have both GPU and CPU-only versions installed simultaneously
Conflicts:      python3-tensorflow
%description -n python3-%{pypi_name}-gpu
tensorflow-gpu for python3 (CUDA)

%prep

%build

%install
pip2 install --no-deps --disable-pip-version-check -I %{SOURCE0} --root %{buildroot} --strip-file-prefix %{buildroot}
cp %{buildroot}/%{_bindir}/tensorboard %{buildroot}/%{_bindir}/tensorboard-2
ln -sf %{_bindir}/tensorboard-2 %{buildroot}/%{_bindir}/tensorboard-%{python2_version}
rm -rf %{buildroot}/%{python2_sitelib}/external
# fix for wheel package weirdness installing to inconsistent package/directory names ("tensorflow" versus "tensorflow-gpu" versus "tensorflow_gpu")
mv %{buildroot}/%{python2_sitearch}/%{pypi_name}_gpu-%{version}.dist-info %{buildroot}/%{python2_sitelib}/%{pypi_name}-%{version}.dist-info
sed -i "s/tensorflow-gpu/tensorflow/" %{buildroot}/%{python2_sitelib}/%{pypi_name}-%{version}.dist-info/metadata.json

pip3 install --no-deps --disable-pip-version-check -I %{SOURCE1} --root %{buildroot} --strip-file-prefix %{buildroot}
cp %{buildroot}/%{_bindir}/tensorboard %{buildroot}/%{_bindir}/tensorboard-3
ln -sf %{_bindir}/tensorboard-3 %{buildroot}/%{_bindir}/tensorboard-%{python3_version}
rm -rf %{buildroot}/%{python3_sitelib}/external
# fix for wheel package weirdness installing to inconsistent package/directory names ("tensorflow" versus "tensorflow-gpu" versus "tensorflow_gpu")
mv %{buildroot}/%{python3_sitearch}/%{pypi_name}_gpu-%{version}.dist-info %{buildroot}/%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
sed -i "s/tensorflow-gpu/tensorflow/" %{buildroot}/%{python2_sitelib}/%{pypi_name}-%{version}.dist-info/metadata.json


%check

%files -n python2-%{pypi_name}-gpu
%{_bindir}/tensorboard-2
%{_bindir}/tensorboard-%{python2_version}
%{python2_sitelib}/%{pypi_name}*

%files -n python3-%{pypi_name}-gpu
%{_bindir}/tensorboard
%{_bindir}/tensorboard-3
%{_bindir}/tensorboard-%{python3_version}
%{python3_sitelib}/%{pypi_name}*


%changelog
* Wed Dec 14 2016 David Goerger - 0.12.0rc1-1
- package tensorflow-gpu
