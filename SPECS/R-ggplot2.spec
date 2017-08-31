%define debug_package %{nil}
%global packname  ggplot2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.1
Release:          1%{?dist}
Summary:          Create Elegant Data Visualisations Using the Grammar of Graphics

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# tbh lazy deps resolution == all R packages that are installed on a working system, regardless of if necessary
Requires:         libxml2
Requires:         tex(latex)
Requires:         R
Requires:         R-ALL
Requires:         R-AnnotationDbi
Requires:         R-BH
Requires:         R-BSgenome
Requires:         R-BSgenome.Celegans.UCSC.ce2
Requires:         R-Biobase
Requires:         R-BiocGenerics
Requires:         R-BiocParallel
Requires:         R-Biostrings
Requires:         R-BufferedMatrix
Requires:         R-BufferedMatrixMethods
Requires:         R-COPASI
Requires:         R-DBI
Requires:         R-DelayedArray
Requires:         R-DynDoc
Requires:         R-GeneR
Requires:         R-GenomeInfoDb
Requires:         R-GenomeInfoDbData
Requires:         R-GenomicAlignments
Requires:         R-GenomicFeatures
Requires:         R-GenomicRanges
Requires:         R-IRanges
Requires:         R-R6
Requires:         R-RCurl
Requires:         R-RInside
Requires:         R-RInside-examples
Requires:         R-RM2
Requires:         R-ROC
Requires:         R-RODBC
Requires:         R-RSQLite
Requires:         R-RUnit
Requires:         R-Rcompression
Requires:         R-Rcpp
Requires:         R-Rcpp-examples
Requires:         R-Rsamtools
Requires:         R-Rsolid
Requires:         R-S4Vectors
Requires:         R-SEDML
Requires:         R-SummarizedExperiment
Requires:         R-TH-data
Requires:         R-XML
Requires:         R-XVector
Requires:         R-abind
Requires:         R-acepack
Requires:         R-affy
Requires:         R-affydata
Requires:         R-affyio
Requires:         R-biglm
Requires:         R-bindr
Requires:         R-bindrcpp
Requires:         R-biomaRt
Requires:         R-bitops
Requires:         R-caTools
Requires:         R-car
Requires:         R-combinat
Requires:         R-core
Requires:         R-crayon
Requires:         R-curl
Requires:         R-devel
Requires:         R-digest
Requires:         R-expm
Requires:         R-fibroEset
Requires:         R-futile.logger
Requires:         R-futile.options
Requires:         R-gtools
Requires:         R-hash
Requires:         R-hgu133acdf
Requires:         R-hgu95av2cdf
Requires:         R-hgu95av2probe
Requires:         R-highlight
Requires:         R-httr
Requires:         R-inline
Requires:         R-java
Requires:         R-jsonlite
Requires:         R-lambda.r
Requires:         R-libSBML
Requires:         R-littler
Requires:         R-littler-examples
Requires:         R-lmtest
Requires:         R-mAr
Requires:         R-maanova
Requires:         R-magrittr
Requires:         R-matrixStats
Requires:         R-memoise
Requires:         R-mime
Requires:         R-msm
Requires:         R-multcomp
Requires:         R-multtest
Requires:         R-mvtnorm
Requires:         R-nws
Requires:         R-openssl
Requires:         R-plogr
Requires:         R-pls
Requires:         R-praise
Requires:         R-preprocessCore
Requires:         R-preprocessCore
Requires:         R-qcc
Requires:         R-qtl
Requires:         R-qvalue
Requires:         R-rlecuyer
Requires:         R-rtracklayer
Requires:         R-sandwich
Requires:         R-sciplot
Requires:         R-shogun
Requires:         R-snow
Requires:         R-statmod
Requires:         R-stockPortfolio
Requires:         R-stringi
Requires:         R-stringr
Requires:         R-swirl
Requires:         R-systemfit
Requires:         R-testthat
Requires:         R-timeDate
Requires:         R-tkWidgets
Requires:         R-waveslim
Requires:         R-wavethresh
Requires:         R-widgetTools
Requires:         R-xtable
Requires:         R-yaml
Requires:         R-zoo
BuildRequires:    chrpath
BuildRequires:    libxml2-devel
BuildRequires:    tex(latex)
BuildRequires:    R-BH
BuildRequires:    R-Biostrings-devel
BuildRequires:    R-BufferedMatrix-devel
BuildRequires:    R-IRanges-devel
BuildRequires:    R-RInside-devel
BuildRequires:    R-Rcpp-devel
BuildRequires:    R-Rsamtools-devel
BuildRequires:    R-Rsolid-devel
BuildRequires:    R-S4Vectors-devel
BuildRequires:    R-XVector-devel
BuildRequires:    R-bindrcpp
BuildRequires:    R-core-devel
BuildRequires:    R-devel
BuildRequires:    R-digest-devel
BuildRequires:    R-java-devel
BuildRequires:    R-mvtnorm-devel
BuildRequires:    R-plogr-devel
BuildRequires:    R-preprocessCore-devel
BuildRequires:    R-zoo-devel
BuildRequires:    R
BuildRequires:    R-ALL
BuildRequires:    R-AnnotationDbi
BuildRequires:    R-BH
BuildRequires:    R-BSgenome
BuildRequires:    R-BSgenome.Celegans.UCSC.ce2
BuildRequires:    R-Biobase
BuildRequires:    R-BiocGenerics
BuildRequires:    R-BiocParallel
BuildRequires:    R-Biostrings
BuildRequires:    R-BufferedMatrix
BuildRequires:    R-BufferedMatrixMethods
BuildRequires:    R-COPASI
BuildRequires:    R-DBI
BuildRequires:    R-DelayedArray
BuildRequires:    R-DynDoc
BuildRequires:    R-GeneR
BuildRequires:    R-GenomeInfoDb
BuildRequires:    R-GenomeInfoDbData
BuildRequires:    R-GenomicAlignments
BuildRequires:    R-GenomicFeatures
BuildRequires:    R-GenomicRanges
BuildRequires:    R-IRanges
BuildRequires:    R-R6
BuildRequires:    R-RCurl
BuildRequires:    R-RInside
BuildRequires:    R-RInside-examples
BuildRequires:    R-RM2
BuildRequires:    R-ROC
BuildRequires:    R-RODBC
BuildRequires:    R-RSQLite
BuildRequires:    R-RUnit
BuildRequires:    R-Rcompression
BuildRequires:    R-Rcpp
BuildRequires:    R-Rcpp-examples
BuildRequires:    R-Rsamtools
BuildRequires:    R-Rsolid
BuildRequires:    R-S4Vectors
BuildRequires:    R-SEDML
BuildRequires:    R-SummarizedExperiment
BuildRequires:    R-TH-data
BuildRequires:    R-XML
BuildRequires:    R-XVector
BuildRequires:    R-abind
BuildRequires:    R-acepack
BuildRequires:    R-affy
BuildRequires:    R-affydata
BuildRequires:    R-affyio
BuildRequires:    R-biglm
BuildRequires:    R-bindr
BuildRequires:    R-bindrcpp
BuildRequires:    R-biomaRt
BuildRequires:    R-bitops
BuildRequires:    R-caTools
BuildRequires:    R-car
BuildRequires:    R-combinat
BuildRequires:    R-core
BuildRequires:    R-crayon
BuildRequires:    R-curl
BuildRequires:    R-devel
BuildRequires:    R-digest
BuildRequires:    R-expm
BuildRequires:    R-fibroEset
BuildRequires:    R-futile.logger
BuildRequires:    R-futile.options
BuildRequires:    R-gtools
BuildRequires:    R-hash
BuildRequires:    R-hgu133acdf
BuildRequires:    R-hgu95av2cdf
BuildRequires:    R-hgu95av2probe
BuildRequires:    R-highlight
BuildRequires:    R-httr
BuildRequires:    R-inline
BuildRequires:    R-java
BuildRequires:    R-jsonlite
BuildRequires:    R-lambda.r
BuildRequires:    R-libSBML
BuildRequires:    R-littler
BuildRequires:    R-littler-examples
BuildRequires:    R-lmtest
BuildRequires:    R-mAr
BuildRequires:    R-maanova
BuildRequires:    R-magrittr
BuildRequires:    R-matrixStats
BuildRequires:    R-memoise
BuildRequires:    R-mime
BuildRequires:    R-msm
BuildRequires:    R-multcomp
BuildRequires:    R-multtest
BuildRequires:    R-mvtnorm
BuildRequires:    R-nws
BuildRequires:    R-openssl
BuildRequires:    R-plogr
BuildRequires:    R-pls
BuildRequires:    R-praise
BuildRequires:    R-preprocessCore
BuildRequires:    R-preprocessCore
BuildRequires:    R-qcc
BuildRequires:    R-qtl
BuildRequires:    R-qvalue
BuildRequires:    R-rlecuyer
BuildRequires:    R-rtracklayer
BuildRequires:    R-sandwich
BuildRequires:    R-sciplot
BuildRequires:    R-shogun
BuildRequires:    R-snow
BuildRequires:    R-statmod
BuildRequires:    R-stockPortfolio
BuildRequires:    R-stringi
BuildRequires:    R-stringr
BuildRequires:    R-swirl
BuildRequires:    R-systemfit
BuildRequires:    R-testthat
BuildRequires:    R-timeDate
BuildRequires:    R-tkWidgets
BuildRequires:    R-waveslim
BuildRequires:    R-wavethresh
BuildRequires:    R-widgetTools
BuildRequires:    R-xtable
BuildRequires:    R-yaml
BuildRequires:    R-zoo


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
%{_bindir}/echo 'install.packages("tidyverse", lib="%{buildroot}%{rlibdir}", repos="https://cran.r-project.org/")' | %{_bindir}/Rscript -
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
# deps - bundling for efficiency, remove and add to RPM 'Requires' above once packaged in Fedora proper
%{rlibdir}/RColorBrewer
%{rlibdir}/assertthat
%{rlibdir}/broom
%{rlibdir}/cellranger
%{rlibdir}/colorspace
%{rlibdir}/dichromat
%{rlibdir}/dplyr
%{rlibdir}/forcats
%{rlibdir}/glue
%{rlibdir}/gtable
%{rlibdir}/haven
%{rlibdir}/hms
%{rlibdir}/labeling
%{rlibdir}/lazyeval
%{rlibdir}/lubridate
%{rlibdir}/mnormt
%{rlibdir}/modelr
%{rlibdir}/munsell
%{rlibdir}/pkgconfig
%{rlibdir}/plyr
%{rlibdir}/psych
%{rlibdir}/purrr
%{rlibdir}/readr
%{rlibdir}/readxl
%{rlibdir}/rematch
%{rlibdir}/reshape2
%{rlibdir}/rlang
%{rlibdir}/rvest
%{rlibdir}/scales
%{rlibdir}/selectr
%{rlibdir}/tibble
%{rlibdir}/tidyr
%{rlibdir}/tidyverse
%{rlibdir}/xml2


%changelog
* Tue Dec 13 2016 deg38 <> 2.2.0-1
- initial package for Fedora
