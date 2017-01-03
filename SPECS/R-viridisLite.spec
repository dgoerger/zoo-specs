%global packname  viridisLite
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Default Color Maps from 'matplotlib' (Lite Version)

Group:            Applications/Engineering 
License:          MIT + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-stats R-grDevices
# Suggests:  R-hexbin R-ggplot2
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core


Requires:         R-stats R-grDevices 
Requires:         R-hexbin R-ggplot2 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-stats R-grDevices 
BuildRequires:   R-hexbin R-ggplot2 

%description
Port of the new 'matplotlib' color maps ('viridis' - the default -,
'magma', 'plasma' and 'inferno') to 'R'. 'matplotlib'
<http://matplotlib.org/ > is a popular plotting library for 'python'.
These color maps are designed in such a way that they will analytically be
perfectly perceptually-uniform, both in regular form and also when
converted to black-and-white. They are also designed to be perceived by
readers with the most common form of color blindness. This is the 'lite'
version of the more complete 'viridis' package that can be found at

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data


%changelog
* Tue Dec 13 2016 deg38 <> 0.1.3-1
- initial package for Fedora
