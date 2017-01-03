%global packname  caret
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          6.0.73
Release:          1%{?dist}
Summary:          Classification and Regression Training

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_6.0-73.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-lattice R-ggplot2
# Imports:   R-car R-foreach R-methods R-plyr R-ModelMetrics R-nlme R-reshape2 R-stats R-stats4 R-utils R-grDevices
# Suggests:  R-BradleyTerry2 R-e1071 R-earth R-fastICA R-gam R-ipred R-kernlab R-klaR R-MASS R-ellipse R-mda R-mgcv R-mlbench R-MLmetrics R-nnet R-party R-pls R-pROC R-proxy R-randomForest R-RANN R-spls R-subselect R-pamr R-superpc R-Cubist R-testthat
# LinkingTo:
# Enhances:


Requires:         R-lattice R-ggplot2 
Requires:         R-car R-foreach R-methods R-plyr R-ModelMetrics R-nlme R-reshape2 R-stats R-stats4 R-utils R-grDevices 
BuildRequires:    R-devel tex(latex) R-lattice R-ggplot2
BuildRequires:    R-car R-foreach R-methods R-plyr R-ModelMetrics R-nlme R-reshape2 R-stats R-stats4 R-utils R-grDevices 

%description
Misc functions for training and plotting classification and regression

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Tue Dec 13 2016 deg38 <> 6.0.73-1
- initial package for Fedora
