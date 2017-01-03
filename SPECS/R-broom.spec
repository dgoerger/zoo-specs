%global packname  broom
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Convert Statistical Analysis Objects into Tidy Data Frames

Group:            Applications/Engineering 
License:          MIT + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Here's the R view of the dependencies world:
# Depends:   
# Imports:   R-plyr R-dplyr R-tidyr R-psych R-stringr R-reshape2 R-nlme R-methods
# Suggests:  R-knitr R-boot R-survival R-gam R-glmnet R-lfe R-Lahman R-MASS R-sp R-maps R-maptools R-multcomp R-testthat R-lme4 R-zoo R-lmtest R-plm R-biglm R-ggplot2 R-nnet R-geepack R-AUC R-ergm R-network R-statnet.common R-xergm R-btergm R-binGroup R-Hmisc R-bbmle R-gamlss R-rstan R-rstanarm R-coda R-gmm R-Matrix R-ks R-purrr R-orcutt R-mgcv R-lmodel2 R-poLCA R-mclust R-covr
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core


Requires:         R-plyr R-dplyr R-tidyr R-psych R-stringr R-reshape2 R-nlme R-methods 
Requires:         R-knitr R-boot R-survival R-gam R-glmnet R-lfe R-Lahman R-MASS R-sp R-maps R-maptools R-multcomp R-testthat R-lme4 R-zoo R-lmtest R-plm R-biglm R-ggplot2 R-nnet R-geepack R-AUC R-ergm R-network R-statnet.common R-xergm R-btergm R-binGroup R-Hmisc R-bbmle R-gamlss R-rstan R-rstanarm R-coda R-gmm R-Matrix R-ks R-purrr R-orcutt R-mgcv R-lmodel2 R-poLCA R-mclust R-covr 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-plyr R-dplyr R-tidyr R-psych R-stringr R-reshape2 R-nlme R-methods 
BuildRequires:   R-knitr R-boot R-survival R-gam R-glmnet R-lfe R-Lahman R-MASS R-sp R-maps R-maptools R-multcomp R-testthat R-lme4 R-zoo R-lmtest R-plm R-biglm R-ggplot2 R-nnet R-geepack R-AUC R-ergm R-network R-statnet.common R-xergm R-btergm R-binGroup R-Hmisc R-bbmle R-gamlss R-rstan R-rstanarm R-coda R-gmm R-Matrix R-ks R-purrr R-orcutt R-mgcv R-lmodel2 R-poLCA R-mclust R-covr 

%description
Convert statistical analysis objects from R into tidy data frames, so that
they can more easily be combined, reshaped and otherwise processed with
tools like 'dplyr', 'tidyr' and 'ggplot2'. The package provides three S3
generics: tidy, which summarizes a model's statistical findings such as
coefficients of a regression; augment, which adds columns to the original
data such as predictions, residuals and cluster assignments; and glance,
which provides a one-row summary of model-level statistics.

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
* Tue Dec 13 2016 deg38 <> 0.4.1-1
- initial package for Fedora