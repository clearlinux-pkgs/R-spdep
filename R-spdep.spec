#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v4
# autospec commit: 213bb01
#
Name     : R-spdep
Version  : 1.3.3
Release  : 72
URL      : https://cran.r-project.org/src/contrib/spdep_1.3-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spdep_1.3-3.tar.gz
Summary  : Spatial Dependence: Weighting Schemes, Statistics
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spdep-lib = %{version}-%{release}
Requires: R-deldir
Requires: R-e1071
Requires: R-s2
Requires: R-sf
Requires: R-sp
Requires: R-spData
Requires: R-units
BuildRequires : R-deldir
BuildRequires : R-e1071
BuildRequires : R-s2
BuildRequires : R-sf
BuildRequires : R-sp
BuildRequires : R-spData
BuildRequires : R-units
BuildRequires : buildreq-R

%description
objects from polygon 'contiguities', from point patterns by distance and
  tessellations, for summarizing these objects, and for permitting their
  use in spatial data analysis, including regional aggregation by minimum
  spanning tree; a collection of tests for spatial 'autocorrelation',
  including global 'Morans I' and 'Gearys C' proposed by 'Cliff' and 'Ord'

%package lib
Summary: lib components for the R-spdep package.
Group: Libraries

%description lib
lib components for the R-spdep package.


%prep
%setup -q -n spdep
pushd ..
cp -a spdep buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707322648

%install
export SOURCE_DATE_EPOCH=1707322648
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/spdep/NEWS.md
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
/usr/lib64/R/library/spdep/doc/index.html
/usr/lib64/R/library/spdep/doc/nb.R
/usr/lib64/R/library/spdep/doc/nb.Rmd
/usr/lib64/R/library/spdep/doc/nb.html
/usr/lib64/R/library/spdep/doc/nb_sf.R
/usr/lib64/R/library/spdep/doc/nb_sf.Rmd
/usr/lib64/R/library/spdep/doc/nb_sf.html
/usr/lib64/R/library/spdep/doc/sids.R
/usr/lib64/R/library/spdep/doc/sids.Rmd
/usr/lib64/R/library/spdep/doc/sids.html
/usr/lib64/R/library/spdep/etc/backstore/boot_res.RData
/usr/lib64/R/library/spdep/etc/backstore/nyME_res.RData
/usr/lib64/R/library/spdep/etc/misc/coords.rda
/usr/lib64/R/library/spdep/etc/misc/geary_eire.txt
/usr/lib64/R/library/spdep/etc/misc/nc_xtra.dbf
/usr/lib64/R/library/spdep/etc/misc/nyadjwts.dbf
/usr/lib64/R/library/spdep/etc/misc/nydata.dbf
/usr/lib64/R/library/spdep/etc/misc/raw_grass_borders.RData
/usr/lib64/R/library/spdep/etc/misc/raw_grass_borders_new.RData
/usr/lib64/R/library/spdep/etc/misc/sids.zip
/usr/lib64/R/library/spdep/etc/misc/sids2.zip
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
/usr/lib64/R/library/spdep/tests/tinytest.R
/usr/lib64/R/library/spdep/tinytest/test_cell2nb.R
/usr/lib64/R/library/spdep/tinytest/test_lisa_perm.R
/usr/lib64/R/library/spdep/tinytest/test_poly2nb_snap.R
/usr/lib64/R/library/spdep/tinytest/test_subgraph_warning.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/spdep/libs/spdep.so
/usr/lib64/R/library/spdep/libs/spdep.so
