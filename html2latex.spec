%include	/usr/lib/rpm/macros.perl
Summary:	HTML to LaTeX converter
Summary(pl):	Konwerter HTML-a do LaTeXa
Name:		html2latex
Version:	1.1
Release:	1
License:	GPL v2+
Group:		Applications/Publishing/TeX
Source0:	http://dl.sourceforge.net/html2latex/%{name}-%{version}.tar.gz
# Source0-md5:	f79c9b9808306cba7d947bbace6f594c
URL:		http://html2latex.sourceforge.net/
%if %{with tests}
BuildRequires:	perl-HTML-Tree >= 2.97
BuildRequires:	perl-XML-Simple >= 1.04
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# optional: perl-libwww, perl-URI, ImageMagick-perl
Requires:	perl-HTML-Latex = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
html2latex uses HTML::TreeBuilder to parse an HTML file and then it
converts the HTML::Element into to a LaTeX file. Each URL will have a
.*html extension stripped. If you use a URL, then the files taken from
the Internet will be stored in your ~/.html2latex directory. If
pictures are included, they are converted to .PNG, which can only be
used with pdflatex. As an added bonus, there is an option to
automatically create a PDF from the LaTeX file (using pdflatex).

%description -l pl
html2latex wykorzystuje HTML::TreeBuilder do analizy plików HTML i
przekszta³acania obiektów HTML::Element do plików LaTeXa. Ka¿dy URL
zostaje pozbawiony rozszerzenia .*html. W przypadku u¿ycia URL-a pliki
pobrane z Internetu zostan± zapisane w katalogu ~/.html2latex.
Za³±czone obrazki s± przekszta³cane do formatu .PNG, który mo¿e byæ
wykorzystany przez pdflatexa. Jako dodatek istnieje opcja
automatycznego tworzenia dokumentu PDF z pliku LaTeXa (przy u¿yciu
pdflatexa).

%package -n perl-HTML-Latex
Summary:	HTML::Latex Perl module - creates a LaTeX file from an HTML file
Summary(pl):	Modu³ Perla HTML::Latex - tworzenie pliku w LaTeXu z pliku HTML
Group:		Development/Languages/Perl
Requires:	perl-HTML-Tree >= 2.97
Requires:	perl-XML-Simple >= 1.04

%description -n perl-HTML-Latex
Converts properly formatted HTML files, filehandles, or strings to
LaTeX. It offers several options in processing, such a the ignoring of
tags, the configuration of the TeX, and downloading of URLs. It is
also much easier to extend than any other html2latex converter.

%description -n perl-HTML-Latex -l pl
Modu³ ten konwertuje odpowiednio sformatowane pliki HTML, uchwyty
plików lub ³añcuchy znaków do LaTeXa. Oferuje przy przetwarzaniu kilka
opcji, takich jak ignorowanie znaczników, konfiguracja TeXa oraz
¶ci±ganie odno¶ników. Jest du¿o prostszy do rozbudowywania ni¿
jakikolwiek inny konwerter html2latex.

%prep
%setup -q

%build
cd HTML

%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C HTML pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install html2latex $RPM_BUILD_ROOT%{_bindir}
install html2latex.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/html2latex
%{_mandir}/man1/html2latex.1*

%files -n perl-HTML-Latex
%defattr(644,root,root,755)
%doc HTML/{Changes,README,TODO}
%{perl_vendorlib}/HTML/Latex.pm
%{_mandir}/man3/HTML::Latex.3*
