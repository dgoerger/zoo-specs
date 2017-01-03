%global packname  rms
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          5.0.1
Release:          1%{?dist}
Summary:          Regression Modeling Strategies

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_5.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   R-Hmisc R-survival R-lattice R-ggplot2 R-SparseM
# Imports:   R-methods R-quantreg R-rpart R-nlme R-polspline R-multcomp R-htmlTable R-htmltools
# Suggests:  R-boot R-tcltk R-plotly
# LinkingTo:
# Enhances:


Requires:         R-Hmisc R-survival R-lattice R-ggplot2 R-SparseM 
Requires:         R-methods R-quantreg R-rpart R-nlme R-polspline R-multcomp R-htmlTable R-htmltools 
Requires:         R-boot R-tcltk R-plotly 
BuildRequires:    R-devel tex(latex) R-Hmisc R-survival R-lattice R-ggplot2 R-SparseM
BuildRequires:    R-methods R-quantreg R-rpart R-nlme R-polspline R-multcomp R-htmlTable R-htmltools 
BuildRequires:   R-boot R-tcltk R-plotly 

%description
Regression modeling, testing, estimation, validation, graphics,
prediction, and typesetting by storing enhanced model design attributes in
the fit.  'rms' is a collection of functions that assist with and
streamline modeling.  It also contains functions for binary and ordinal
logistic regression models, ordinal models for continuous Y with a variety
of distribution families, and the Buckley-James multiple regression model
for right-censored responses, and implements penalized maximum likelihood
estimation for logistic and ordinary linear models.  'rms' works with
almost any regression model, but it was especially written to work with
binary or ordinal regression models, Cox regression, accelerated failure
time models, ordinary linear models,	the Buckley-James model, generalized
least squares for serially or spatially correlated observations,
generalized linear models, and quantile regression.

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
* Tue Dec 13 2016 deg38 <> 5.0.1-1
- initial package for Fedora