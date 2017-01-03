%define debug_package %{nil}
%global packname  ggplot2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.0
Release:          1%{?dist}
Summary:          Create Elegant Data Visualisations Using the Grammar of Graphics

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-digest R-grid R-gtable R-MASS R-plyr R-reshape2 R-scales R-stats R-tibble R-lazyeval
# Suggests:  R-covr R-ggplot2movies R-hexbin R-Hmisc R-lattice R-mapproj R-maps R-maptools R-mgcv R-multcomp R-nlme R-testthat R-quantreg R-knitr R-rpart R-rmarkdown R-svglite
# LinkingTo:
# Enhances:



Requires:         R-digest R-grid R-gtable R-MASS R-plyr R-reshape2 R-scales R-stats R-tibble R-lazyeval 
Requires:         R-covr R-ggplot2movies R-hexbin R-lattice R-mapproj R-maps R-maptools R-mgcv R-multcomp R-nlme R-testthat R-quantreg R-knitr R-rpart R-rmarkdown R-svglite 
Recommends:       R-Hmisc
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-digest R-grid R-gtable R-MASS R-plyr R-reshape2 R-scales R-stats R-tibble R-lazyeval 
BuildRequires:   R-covr R-ggplot2movies R-hexbin R-lattice R-mapproj R-maps R-maptools R-mgcv R-multcomp R-nlme R-testthat R-quantreg R-knitr R-rpart R-rmarkdown R-svglite 

%description
A system for 'declaratively' creating graphics, based on "The Grammar of
Graphics". You provide the data, tell 'ggplot2' how to map variables to
aesthetics, what graphical primitives to use, and it takes care of the

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

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data


%changelog
* Tue Dec 13 2016 deg38 <> 2.2.0-1
- initial package for Fedora
