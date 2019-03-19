#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spdep
Version  : 1.0.2
Release  : 24
URL      : https://cran.r-project.org/src/contrib/spdep_1.0-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spdep_1.0-2.tar.gz
Summary  : Spatial Dependence: Weighting Schemes, Statistics and Models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spdep-lib = %{version}-%{release}
Requires: R-DBI
Requires: R-Rcpp
Requires: R-classInt
Requires: R-units
BuildRequires : R-DBI
BuildRequires : R-LearnBayes
BuildRequires : R-RANN
BuildRequires : R-Rcpp
BuildRequires : R-classInt
BuildRequires : R-coda
BuildRequires : R-deldir
BuildRequires : R-e1071
BuildRequires : R-expm
BuildRequires : R-gdata
BuildRequires : R-gmodels
BuildRequires : R-gtools
BuildRequires : R-maptools
BuildRequires : R-sf
BuildRequires : R-sp
BuildRequires : R-spData
BuildRequires : R-units
BuildRequires : buildreq-R

%description
Spatial dependence: weighting schemes, statistics and models
A collection of functions to create spatial weights matrix objects from
polygon contiguities, from point patterns by distance and tesselations,
for summarising these objects, and for permitting their use in spatial
data analysis; a collection of tests for spatial autocorrelation,
including global Moran's I, Geary's C, Hubert/Mantel general cross product
statistic, Empirical Bayes estimates and spatial Index, and Getis/Ord G,
local Moran's I and Getis/Ord G, saddlepoint approximations for global
and local Moran's I; and functions for estimating spatial simultaneous
autoregressive (SAR) lag and error models, weighted and unweighted
SAR and CAR spatial regression models, and GM SAR error models.

%package lib
Summary: lib components for the R-spdep package.
Group: Libraries

%description lib
lib components for the R-spdep package.


%prep
%setup -q -c -n spdep

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552962464

%install
export SOURCE_DATE_EPOCH=1552962464
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spdep
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spdep
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spdep
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  spdep || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spdep/CHANGES
/usr/lib64/R/library/spdep/CITATION
/usr/lib64/R/library/spdep/ChangeLog
/usr/lib64/R/library/spdep/DESCRIPTION
/usr/lib64/R/library/spdep/INDEX
/usr/lib64/R/library/spdep/Meta/Rd.rds
/usr/lib64/R/library/spdep/Meta/data.rds
/usr/lib64/R/library/spdep/Meta/features.rds
/usr/lib64/R/library/spdep/Meta/hsearch.rds
/usr/lib64/R/library/spdep/Meta/links.rds
/usr/lib64/R/library/spdep/Meta/nsInfo.rds
/usr/lib64/R/library/spdep/Meta/package.rds
/usr/lib64/R/library/spdep/Meta/vignette.rds
/usr/lib64/R/library/spdep/NAMESPACE
/usr/lib64/R/library/spdep/R/spdep
/usr/lib64/R/library/spdep/R/spdep.rdb
/usr/lib64/R/library/spdep/R/spdep.rdx
/usr/lib64/R/library/spdep/README
/usr/lib64/R/library/spdep/data/columbus.rda
/usr/lib64/R/library/spdep/data/eire.rda
/usr/lib64/R/library/spdep/data/oldcol.rda
/usr/lib64/R/library/spdep/doc/CO69.R
/usr/lib64/R/library/spdep/doc/CO69.Rmd
/usr/lib64/R/library/spdep/doc/CO69.html
/usr/lib64/R/library/spdep/doc/SpatialFiltering.R
/usr/lib64/R/library/spdep/doc/SpatialFiltering.Rmd
/usr/lib64/R/library/spdep/doc/SpatialFiltering.html
/usr/lib64/R/library/spdep/doc/index.html
/usr/lib64/R/library/spdep/doc/nb.R
/usr/lib64/R/library/spdep/doc/nb.Rnw
/usr/lib64/R/library/spdep/doc/nb.pdf
/usr/lib64/R/library/spdep/doc/nb_igraph.R
/usr/lib64/R/library/spdep/doc/nb_igraph.Rmd
/usr/lib64/R/library/spdep/doc/nb_igraph.html
/usr/lib64/R/library/spdep/doc/nb_sf.R
/usr/lib64/R/library/spdep/doc/nb_sf.Rmd
/usr/lib64/R/library/spdep/doc/nb_sf.html
/usr/lib64/R/library/spdep/doc/sids.R
/usr/lib64/R/library/spdep/doc/sids.Rmd
/usr/lib64/R/library/spdep/doc/sids.html
/usr/lib64/R/library/spdep/etc/backstore/boot_res.RData
/usr/lib64/R/library/spdep/etc/backstore/nyME_res.RData
/usr/lib64/R/library/spdep/etc/misc/geary_eire.txt
/usr/lib64/R/library/spdep/etc/misc/nc_xtra.dbf
/usr/lib64/R/library/spdep/etc/misc/nyadjwts.dbf
/usr/lib64/R/library/spdep/etc/misc/nydata.dbf
/usr/lib64/R/library/spdep/etc/misc/raw_grass_borders.RData
/usr/lib64/R/library/spdep/etc/misc/unstand_sn.txt
/usr/lib64/R/library/spdep/etc/shapes/bhicv.dbf
/usr/lib64/R/library/spdep/etc/shapes/bhicv.shp
/usr/lib64/R/library/spdep/etc/shapes/bhicv.shx
/usr/lib64/R/library/spdep/etc/shapes/columbus.dbf
/usr/lib64/R/library/spdep/etc/shapes/columbus.shp
/usr/lib64/R/library/spdep/etc/shapes/columbus.shx
/usr/lib64/R/library/spdep/etc/shapes/eire.dbf
/usr/lib64/R/library/spdep/etc/shapes/eire.shp
/usr/lib64/R/library/spdep/etc/shapes/eire.shx
/usr/lib64/R/library/spdep/etc/weights/columbus.gal
/usr/lib64/R/library/spdep/etc/weights/us48.txt
/usr/lib64/R/library/spdep/etc/weights/us48_q.GAL
/usr/lib64/R/library/spdep/etc/weights/us48_rk.GAL
/usr/lib64/R/library/spdep/etc/weights/wmat.dat
/usr/lib64/R/library/spdep/help/AnIndex
/usr/lib64/R/library/spdep/help/aliases.rds
/usr/lib64/R/library/spdep/help/paths.rds
/usr/lib64/R/library/spdep/help/spdep.rdb
/usr/lib64/R/library/spdep/help/spdep.rdx
/usr/lib64/R/library/spdep/html/00Index.html
/usr/lib64/R/library/spdep/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/spdep/libs/spdep.so
/usr/lib64/R/library/spdep/libs/spdep.so.avx2
/usr/lib64/R/library/spdep/libs/spdep.so.avx512
