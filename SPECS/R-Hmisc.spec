%global packname  Hmisc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.17
Release:          4%{?dist}
Summary:          Harrell Miscellaneous

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.17-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-lattice R-survival R-Formula R-ggplot2
# Imports:   R-methods R-latticeExtra R-cluster R-rpart R-nnet R-acepack R-foreign R-gtable R-grid R-gridExtra R-data.table R-htmlTable R-viridis R-htmltools R-base64
# Suggests:  R-chron R-rms R-mice R-tables R-knitr R-ff R-ffbase R-plotly
# LinkingTo:
# Enhances:


Requires:         R-lattice R-survival R-Formula R-ggplot2 
Requires:         R-methods R-latticeExtra R-rpart R-nnet R-acepack R-foreign R-gtable R-grid R-gridExtra R-data.table R-htmlTable R-viridis R-htmltools R-base64 
BuildRequires:    R-devel tex(latex) R-lattice R-survival R-Formula
BuildRequires:    R-methods R-latticeExtra R-rpart R-nnet R-acepack R-foreign R-gtable R-grid R-gridExtra R-data.table R-htmlTable R-viridis R-htmltools R-base64 

%description
Contains many functions useful for data analysis, high-level graphics,
utility operations, functions for computing sample size and power,
importing and annotating datasets, imputing missing values, advanced table
making, variable clustering, character string manipulation, conversion of
R objects to LaTeX and html code, and recoding variables.

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
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/CHANGELOG
%{rlibdir}/%{packname}/THANKS
%{rlibdir}/%{packname}/WISHLIST
%{rlibdir}/%{packname}/todo
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Tue Dec 13 2016 deg38 <> 4.0.1-1
- initial package for Fedora
