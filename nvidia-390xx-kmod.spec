# buildforkernels macro hint: when you build a new version or a new release
# that contains bugfixes or other improvements then you must disable the
# "buildforkernels newest" macro for just that build; immediately after
# queuing that build enable the macro again for subsequent builds; that way
# a new akmod package will only get build when a new one is actually needed
%if 0%{?fedora}
%bcond_with kmod

%if %{with kmod}
%global buildforkernels current
%else
%global buildforkernels akmod
%endif
%endif
%global debug_package %{nil}

Name:          nvidia-390xx-kmod
Epoch:         3
Version:       390.157
# Taken over by kmodtool
Release:       19%{?dist}
Summary:       NVIDIA 390xx display driver kernel module
Group:         System Environment/Kernel
License:       Redistributable, no modification permitted
URL:           http://www.nvidia.com/

Source11:      nvidia-390xx-kmodtool-excludekernel-filterfile

# Patches partially sourced from
#  Debian   https://salsa.debian.org/nvidia-team/nvidia-graphics-drivers/-/tree/390xx/master/debian/module/debian/patches
#  Arch     https://aur.archlinux.org/packages/nvidia-390xx-dkms/
#           https://gitlab.com/herecura/packages/nvidia-390xx-dkms/
#  openSUSE https://build.opensuse.org/package/show/home:luc14n0:nvidia/nvidia-gfxG04

# kernel support
Patch12: do-div-cast.patch
Patch13: 0018-backport-nv_install_notifier-changes-from-418.30.patch
#Copied from Arch
Patch19:  kernel-4.16+-memory-encryption.patch
Patch20:  nvidia-390xx-kmod-0024-kernel-6.2-adaptation.patch
Patch21:  nvidia-390xx-kmod-0025-kernel-6.3-adaptation.patch
Patch22:  nvidia-390xx-kmod-0026-kernel-6.4-adaptation.patch
Patch23:  nvidia-390xx-kmod-0027-kernel-6.5-garbage-collect-all-references-to-get_user.patch
Patch24:  nvidia-390xx-kmod-0028-kernel-6.5-handle-get_user_pages-vmas-argument-remova.patch
Patch25:  nvidia-390xx-kmod-0029-kernel-6.6-backport-drm_gem_prime_handle_to_fd-changes-from-470.patch
Patch26:  nvidia-390xx-kmod-0030-kernel-6.6-refuse-to-load-legacy-module-if-IBT-is-enabled.patch
Patch27:  nvidia-390xx-kmod-0031-kernel-6.8-adaptation.patch
Patch28:  nvidia-390xx-kmod-0032-kernel-6.8-conftest_h-wait_on_bit_lock.patch
Patch29:  nvidia-390xx-kmod-0033-kernel-5.6-ioremap_nocache_removed.patch
Patch100: nvidia-390xx-kmod-0034-kernel-5.9-dma_is_direct-removed.patch
Patch101: nvidia-390xx-kmod-0035-gcc14-no-previous-prototype-for-nv_load_dma_map_scatterlist.patch
Patch102: nvidia-390xx-kmod-0036-undef-NV_ACPI_BUS_GET_DEVICE_PRESENT-in-conftest_sh.patch
Patch103: nvidia-390xx-kmod-0037-add-RPM_CFLAGS-setup-in-conftest_sh.patch
Patch104: nvidia-390xx-kmod-0038-workaround-NV_EFI_ENABLED-macro.patch
Patch105: nvidia-390xx-kmod-0039-incompatible-function-type-nv_gpu_numa_c.patch
Patch106: nvidia-390xx-kmod-0040-fix-fallthrough-warning-nv_mmap_c.patch
Patch107: nvidia-390xx-kmod-0041-no-previous-prototype-for-exercise_error_forwarding_va.patch
Patch108: nvidia-390xx-kmod-0042-undef-NV_DO_GETTIMEOFDAY_PRESENT-in-conftest_sh.patch
Patch109: nvidia-390xx-kmod-0043-undef-NV_SET_MEMORY_ARRAY_UC_PRESENT-in-conftest_sh.patch
Patch110: nvidia-390xx-kmod-0044-undef-NV_ACQUIRE_CONSOLE_SEM_PRESENT-in-conftest_sh.patch
Patch111: nvidia-390xx-kmod-0045-undef-NV_UNSAFE_FOLLOW_PFN_PRESENT-in-conftest_sh.patch
Patch112: nvidia-390xx-kmod-0046-undef-NV_JIFFIES_TO_TIMESPEC_PRESENT-in-conftest_sh.patch
Patch113: nvidia-390xx-kmod-0047-undef-NV_PNV_NPU2_INIT_CONTEXT_PRESENT-in-conftest_sh.patch
Patch114: nvidia-390xx-kmod-0048-fix-atomic64-include-in-conftest_sh.patch
Patch115: nvidia-390xx-kmod-0049-fix-dma_buf_map-renamed-to-iosys_map.patch
Patch116: nvidia-390xx-kmod-0050-no-previous-prototype-for-nv_pci_register_driver.patch
Patch117: nvidia-390xx-kmod-0051-no-previous-prototype-for-nvidia_init_exit_module-in-nv_c.patch
Patch118: nvidia-390xx-kmod-0052-no-previous-prototype-for-on_nv_assert.patch
Patch119: nvidia-390xx-kmod-0053-no-previous-prototype-for-_raw_q_flush.patch
Patch120: nvidia-390xx-kmod-0054-no-previous-prototype-for-nv-ibmnpu-functions.patch
Patch121: nvidia-390xx-kmod-0055-no-previous-prototype-for-uvm_tools_init_exit.patch
Patch122: nvidia-390xx-kmod-0056-no-previous-prototype-for-uvm8_test_set_prefetch_filtering.patch
Patch123: nvidia-390xx-kmod-0057-no-previous-prototype-in-uvm8_va_space_c.patch
Patch124: nvidia-390xx-kmod-0058-no-previous-prototype-for-uvm_channel_manager_print_pending_pushes.patch
Patch125: nvidia-390xx-kmod-0059-no-previous-prototype-in-uvm8_va_range_c.patch
Patch126: nvidia-390xx-kmod-0060-no-previous-prototype-in-uvm8_range_group_c.patch
Patch127: nvidia-390xx-kmod-0061-no-previous-prototype-in-uvm8_gpu_replayable_faults_c.patch
Patch128: nvidia-390xx-kmod-0062-no-previous-prototype-for-block_map.patch
Patch129: nvidia-390xx-kmod-0063-no-previous-prototype-for-try_get_ptes.patch
Patch130: nvidia-390xx-kmod-0064-no-previous-prototype-in-uvm8_pushbuffer_c.patch
Patch131: nvidia-390xx-kmod-0065-no-previous-prototype-in-uvm8_kepler_mmu_c.patch
Patch132: nvidia-390xx-kmod-0066-no-previous-prototype-in-uvm8_pascal_mmu_c.patch
Patch133: nvidia-390xx-kmod-0067-no-previous-prototype-for-parse_fault_entry_common.patch
Patch134: nvidia-390xx-kmod-0068-no-previous-prototype-in-uvm8_volta_access_counter_buffer_c.patch
Patch135: nvidia-390xx-kmod-0069-no-previous-prototype-for-va_block_set_read_duplication_locked.patch
Patch136: nvidia-390xx-kmod-0070-no-previous-prototype-for-map_rm_pt_range.patch
Patch137: nvidia-390xx-kmod-0071-no-previous-prototype-in-uvm8_user_channel_c.patch
Patch138: nvidia-390xx-kmod-0072-no-previous-prototype-in-uvm8_perf_thrashing_c.patch
Patch139: nvidia-390xx-kmod-0073-no-previous-prototype-in-uvm8_perf_prefetch_c.patch
Patch140: nvidia-390xx-kmod-0074-no-previous-prototype-for-test_tracking.patch
Patch141: nvidia-390xx-kmod-0075-no-previous-prototype-in-uvm8_page_tree_test_c.patch
Patch142: nvidia-390xx-kmod-0076-no-previous-prototype-in-uvm8_tracker_test_c.patch
Patch143: nvidia-390xx-kmod-0077-no-previous-prototype-in-uvm8_push_test_c.patch
Patch144: nvidia-390xx-kmod-0078-no-previous-prototype-in-uvm8_channel_test_c.patch
Patch145: nvidia-390xx-kmod-0079-no-previous-prototype-in-nvidia-modeset-linux_c.patch
Patch146: nvidia-390xx-kmod-0080-fix-enum-implicit-conversion-from-uvm_fault_type_t-to-uvm_fault_access_type_t-in-uvm8_va_range_c.patch
Patch147: nvidia-390xx-kmod-0081-fix-enum-implicit-conversion-from-uvm_fault_access_type_t-to-uvm_fault_type_t-in-uvm8_gpu_replayable_faults_c.patch
Patch148: nvidia-390xx-kmod-0082-fix-enum-implicit-conversion-from-uvm_fault_access_type_t-to-uvm_fault_type_t-in-uvm8_gpu_non_replayable_faults_c.patch
Patch149: nvidia-390xx-kmod-0083-fix-enum-implicit-conversion-from-uvm_fault_access_type_t-to-uvm_fault_type_t-in-uvm8_va_block_c.patch
Patch150: nvidia-390xx-kmod-0084-no-previous-prototype-in-nvlink_linux_c.patch
Patch151: nvidia-390xx-kmod-0085-undef-NV_DRM_GEM_OBJECT_PUT_UNLOCK_PRESENT-in-conftest_sh.patch
Patch152: nvidia-390xx-kmod-0086-undef-NV_DRM_CONNECTOR_FUNCS_HAVE_MODE_IN_NAME-in-conftest_sh.patch
Patch153: nvidia-390xx-kmod-0087-undef-NV_DRM_REINIT_PRIMARY_MODE_GROUP_PRESENT-in-conftest_sh.patch
Patch154: nvidia-390xx-kmod-0088-undef-NV_DRM_ATOMIC_HELPER_CONNECTOR_DPMS_PRESENT-in-conftest_sh.patch
Patch155: nvidia-390xx-kmod-0089-kernel-6.10-removed-follow_pfn-function.patch
Patch156: nvidia-390xx-kmod-0090-fix_warning_suggested_braces_around_empty_body_in_if.patch
Patch157: nvidia-390xx-kmod-0091-fix_warning_old_style_declaration_.patch
Patch158: nvidia-390xx-kmod-0092-fix_index_0_is_out_of_range_kernel_6.8_traces.patch
Patch159: nvidia-390xx-kmod-0093-kernel-6.12-adaptation.patch
Patch160: nvidia-390xx-kmod-0094-kernel-6.13-kbuild-external-module-source-tree-change.patch
Patch161: nvidia-390xx-kmod-0095-kernel-6.14-date-removed-from-struct-drm_driver.patch
Patch162: nvidia-390xx-kmod-0096-kernel-6.15-replace_EXTRA_CFLAGS_with_ccflags-y.patch
Patch163: nvidia-390xx-kmod-0097-kernel-6.15-add_MODULE_DESCRIPTION_macro.patch
Patch164: nvidia-390xx-kmod-0098-kernel-6.15-fix_gcc-15_std_gnu17.patch
Patch165: nvidia-390xx-kmod-0099-kernel-6.15-struct_drm_display_mode_to_const.patch
Patch166: nvidia-390xx-kmod-0100-kernel-6.15-convert_del_timer_sync_to_timer_delete_sync.patch
Patch167: nvidia-390xx-kmod-0101-kernel-6.15-switch_vm_flags_set_and_vm_flags_clear_to_vm_flags_reset.patch

# build system updates
Patch30: use-kbuild-compiler.patch
Patch31: conftest-verbose.patch
Patch32: cc_version_check-gcc5.patch
Patch33: bashisms.patch

# armhf support
Patch40: include-swiotlb-header-on-arm.patch
Patch41: ignore_xen_on_arm.patch
Patch42: arm-outer-sync.patch
Patch43: nvidia-drm-arm-cflags.patch

# needed for plague to make sure it builds for i586 and i686
ExclusiveArch:  i686 x86_64 armv7hl

# get the needed BuildRequires (in parts depending on what we build for)
%global AkmodsBuildRequires %{_bindir}/kmodtool, xorg-x11-drv-nvidia-390xx-kmodsrc >= %{epoch}:%{version}
BuildRequires:  %{AkmodsBuildRequires}

%{!?kernels:BuildRequires: gcc, elfutils-libelf-devel, buildsys-build-rpmfusion-kerneldevpkgs-%{?buildforkernels:%{buildforkernels}}%{!?buildforkernels:current}-%{_target_cpu} }
# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo rpmfusion --kmodname %{name} --filterfile %{SOURCE11} --obsolete-name nvidia --obsolete-version "%{?epoch}:%{version}" %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }


%description
The nvidia 390xx %{version} display driver kernel module for kernel %{kversion}.

Important warning: this module has reached the end of support from NVidia.
It is therefore exposed to Common Vulnerabilities and Exposures (CVE).
More information on the concerned CVE could be obtained here:
https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=NVIDIA+390.157+linux
https://www.nvidia.com/en-us/security/


%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}
# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu}  --repo rpmfusion --kmodname %{name} --filterfile %{SOURCE11} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null
%setup -T -c
tar --use-compress-program xz -xf %{_datadir}/%{name}-%{version}/%{name}-%{version}-%{_target_cpu}.tar.xz
# Apply patches
%patch -P 12 -p1 -b 12 -d kernel
%patch -P 13 -p1 -b 13 -d kernel
%patch -P 19 -p1 -b 19
%patch -P 20 -p1 -b 20
%patch -P 21 -p1 -b 21
%patch -P 22 -p1 -b 22
%patch -P 23 -p1 -b 23 -d kernel
%patch -P 24 -p1 -b 24 -d kernel
%patch -P 25 -p1 -b 25 -d kernel
%patch -P 26 -p1 -b 26 -d kernel
%patch -P 27 -p1 -b 27 -d kernel
%patch -P 28 -p1 -b 28 -d kernel
%patch -P 29 -p1 -b 29 -d kernel
%patch -P 100 -p1 -b 100 -d kernel
%patch -P 101 -p1 -b 101 -d kernel
%patch -P 102 -p1 -b 102 -d kernel
%patch -P 103 -p1 -b 103 -d kernel
%patch -P 104 -p1 -b 104 -d kernel
%patch -P 105 -p1 -b 105 -d kernel
%patch -P 106 -p1 -b 106 -d kernel
%patch -P 107 -p1 -b 107 -d kernel
%patch -P 108 -p1 -b 108 -d kernel
%patch -P 109 -p1 -b 109 -d kernel
%patch -P 110 -p1 -b 110 -d kernel
%patch -P 111 -p1 -b 111 -d kernel
%patch -P 112 -p1 -b 112 -d kernel
%patch -P 113 -p1 -b 113 -d kernel
%patch -P 114 -p1 -b 114 -d kernel
%patch -P 115 -p1 -b 115 -d kernel
%patch -P 116 -p1 -b 116 -d kernel
%patch -P 117 -p1 -b 117 -d kernel
%patch -P 118 -p1 -b 118 -d kernel
%patch -P 119 -p1 -b 119 -d kernel
%patch -P 120 -p1 -b 120 -d kernel
%patch -P 121 -p1 -b 121 -d kernel
%patch -P 122 -p1 -b 122 -d kernel
%patch -P 123 -p1 -b 123 -d kernel
%patch -P 124 -p1 -b 124 -d kernel
%patch -P 125 -p1 -b 125 -d kernel
%patch -P 126 -p1 -b 126 -d kernel
%patch -P 127 -p1 -b 127 -d kernel
%patch -P 128 -p1 -b 128 -d kernel
%patch -P 129 -p1 -b 129 -d kernel
%patch -P 130 -p1 -b 130 -d kernel
%patch -P 131 -p1 -b 131 -d kernel
%patch -P 132 -p1 -b 132 -d kernel
%patch -P 133 -p1 -b 133 -d kernel
%patch -P 134 -p1 -b 134 -d kernel
%patch -P 135 -p1 -b 135 -d kernel
%patch -P 136 -p1 -b 136 -d kernel
%patch -P 137 -p1 -b 137 -d kernel
%patch -P 138 -p1 -b 138 -d kernel
%patch -P 139 -p1 -b 139 -d kernel
%patch -P 140 -p1 -b 140 -d kernel
%patch -P 141 -p1 -b 141 -d kernel
%patch -P 142 -p1 -b 142 -d kernel
%patch -P 143 -p1 -b 143 -d kernel
%patch -P 144 -p1 -b 144 -d kernel
%patch -P 145 -p1 -b 145 -d kernel
%patch -P 146 -p1 -b 146 -d kernel
%patch -P 147 -p1 -b 147 -d kernel
%patch -P 148 -p1 -b 148 -d kernel
%patch -P 149 -p1 -b 149 -d kernel
%patch -P 150 -p1 -b 150 -d kernel
%patch -P 151 -p1 -b 151 -d kernel
%patch -P 152 -p1 -b 152 -d kernel
%patch -P 153 -p1 -b 153 -d kernel
%patch -P 154 -p1 -b 154 -d kernel

%patch -P 30 -p1 -b 30 -d kernel
%patch -P 31 -p1 -b 31 -d kernel
%patch -P 32 -p1 -b 32 -d kernel
%patch -P 33 -p1 -b 33 -d kernel

%patch -P 155 -p1 -b 155
%patch -P 156 -p1 -b 156
%patch -P 157 -p1 -b 157
%patch -P 158 -p1 -b 158
%patch -P 159 -p1 -b 159
%patch -P 160 -p1 -b 160
%patch -P 161 -p1 -b 161
%patch -P 162 -p1 -b 162
%patch -P 163 -p1 -b 163
%patch -P 164 -p1 -b 164
%patch -P 165 -p1 -b 165
%patch -P 166 -p1 -b 166
%patch -P 167 -p1 -b 167

%ifarch armv7hl
%patch -P 40 -p1 -b 40 -d kernel
%patch -P 41 -p1 -b 41 -d kernel
%patch -P 42 -p1 -b 42 -d kernel
%patch -P 43 -p1 -b 43 -d kernel
%endif

for kernel_version  in %{?kernel_versions} ; do
    cp -a kernel _kmod_build_${kernel_version%%___*}
done


%build
for kernel_version in %{?kernel_versions}; do
  pushd _kmod_build_${kernel_version%%___*}/
    make V=1 %{?_smp_mflags} \
	    RPM_CFLAGS="%{optflags}" \
        KERNEL_UNAME="${kernel_version%%___*}" SYSSRC="${kernel_version##*___}" \
        IGNORE_CC_MISMATCH=1 IGNORE_XEN_PRESENCE=1 IGNORE_PREEMPT_RT_PRESENCE=1 \
        module
  popd
done


%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p  $RPM_BUILD_ROOT/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -D -m 0755 _kmod_build_${kernel_version%%___*}/nvidia*.ko \
         $RPM_BUILD_ROOT/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}


%changelog
* Wed Jun 18 2025 Nicolas Viéville <nicolas.vieville@uphf.fr> - 3:390.157-19
- gcc-15: move force build to use std=gnu17 from SPEC file to NVidia sources
- kernel >= 6.15: Kbuild: replace EXTRA_CFLAGS with ccflags-y
- kernel >= 6.15: add MODULE_DESCRIPTION macro
- kernel >= 6.15: nvidia-drm-connector.c: struct drm_display_mode to const
- kernel >= 6.15: convert del_timer_sync to timer_delete_sync
- kernel >= 6.15: switch vm_flags_set and vm_flags_clear to vm_flags_reset

* Fri Apr 11 2025 Leigh Scott <leigh123linux@gmail.com> - 3:390.157-18
- Fix up last commit

* Fri Apr 11 2025 Leigh Scott <leigh123linux@gmail.com> - 3:390.157-17
- Force build to use std=gnu17

* Sun Feb 16 2025 Nicolas Viéville <nicolas.vieville@uphf.fr> - 3:390.157-16
- Add patch for kernel >= 6.13
- Add patch for kernel >= 6.14

* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3:390.157-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 16 2024 Nicolas Viéville <nicolas.vieville@uphf.fr> - 3:390.157-14
- Fix patch for kernel >= 6.12 - needs DRM kernel mode setting enabled via
  nvidia-drm.modeset=1

* Sat Dec 14 2024 Nicolas Viéville <nicolas.vieville@uphf.fr> - 3:390.157-13
- Add patch for kernel >= 6.12

* Sat Oct 05 2024 Nicolas Viéville <nicolas.vieville@uphf.fr> - 3:390.157-12
- Fix for 'index 0 is out of range for type 'uvm_gpu_chunk_t *[*]' and
  uvm_page_directory_t *[*]' traces from kernel 6.8.x - RFBZ#7069
  Thanks to Bruce Jerrick

* Mon Aug 19 2024 Nicolas Viéville <nicolas.vieville@uphf.fr> - 3:390.157-11
- Add patch for kernel >= 6.10 - RFBZ#7022
- Fix warning: suggest braces around empty body in an ‘if’ statement
- Fix warning: old style declaration

* Sat Aug 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3:390.157-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 19 2024 Nicolas Viéville <nicolas.vieville@uphf.fr> - 3:390.157-9
- Try to fix errors and warnings for Fedora 40 and gcc14 - RFBZ#6905
  Can't fix "Please avoid flushing system-wide workqueues" warning as
  destroy_workqueue and alloc_workqueue functions are GPL only symbols
- Fixed previous patches - Hunk offsets
- SPEC file clean-up
- Added CVE warning to description in SPEC file
- Important warning: this module has reached the end of support from NVidia
  It is therefore exposed to Common Vulnerabilities and Exposures (CVE).
  More information on the concerned CVE could be obtained here:
  https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=NVIDIA+390.157+linux
  https://www.nvidia.com/en-us/security/

* Sat Apr 06 2024 Nicolas Viéville <nicolas.vieville@uphf.fr> - 3:390.157-8
- Add patch for kernel >= 6.8

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3:390.157-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 02 2023 Nicolas Viéville <nicolas.vieville@uphf.fr> - 3:390.157-6
- Renamed kernel 6.5 patches
- Add patch for kernel >= 6.6 - RFBZ#6802
- Add patch for disabling module loading when Indirect Branch Tracking is active

* Tue Sep 12 2023 Leigh Scott <leigh123linux@gmail.com> - 3:390.157-5
- Add patch for kernel >= 6.5

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3:390.157-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 01 2023 Nicolas Viéville <nicolas.vieville@uphf.fr> - 3:390.157-3
- Fix patch for kernel >= 6.2
- Add patch for kernel >= 6.3
- Add patch for kernel >= 6.4
- SPEC file - Fix patchN macro is deprecated

* Wed Apr 12 2023 Nicolas Viéville <nicolas.vieville@uphf.fr> - 3:390.157-2
- Add patch for kernel >= 6.2

* Sat Jan 07 2023 Henrik Nordstrom <henrik@henriknordstrom.net> - 3:390.157-1
- Update to 390.157

* Thu Nov 03 2022 Leigh Scott <leigh123linux@gmail.com> - 3:390.154-3
- Patch for 6.0 kernel
- Clean up old patches

* Sun Aug 28 2022 Leigh Scott <leigh123linux@gmail.com> - 3:390.154-2
- Restore kmod for el build

* Sun Aug 28 2022 Leigh Scott <leigh123linux@gmail.com> - 3:390.154-1
- Update to 390.154 release

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3:390.151-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Sat Jun 18 2022 Henrik Nordstrom <henrik@henriknordstrom.net> - 390.151-1
- Update to 390.151

* Wed Apr 20 2022 Sérgio Basto <sergio@serjux.com> - 3:390.147-3
- Try to fix linux-5.17 based on patch provided on https://bugzilla.rpmfusion.org/6263

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3:390.147-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 29 2022 Henrik Nordstrom <henrik@henriknordstrom.net> - 390.147-1
- Update to 390.147

* Wed Sep 22 2021 Henrik Nordstrom <henrik@henriknordstrom.net> - 390.144-3
- Kernel 5.14 patch taken from openSUSE

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3:390.144-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 23 2021 Henrik Nordstrom <henrik@henriknordstrom.net> - 390.144-1
- Update to 390.144

* Sun Jun 27 2021 Henrik Nordstrom <henrik@henriknordstrom.net> - 390.143-2
- Kernel 5.12 patch taken from openSUSE via Arch repo
- Kernel 5.13 patch taken from Herecura Arch repo

* Tue Apr 20 2021 Henrik Nordstrom <henrik@henriknordstrom.net> - 390.143-1
- Update to 390.143

* Mon Mar 22 2021 Henrik Nordstrom <henrik@henriknordstrom.net> - 390.141-6
- Update patches from Debian.

* Mon Mar 22 2021 Henrik Nordstrom <henrik@henriknordstrom.net> - 3:390.141-5
- Patch for kernel 5.11 (Bug #5951)

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3:390.141-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Leigh Scott <leigh123linux@gmail.com> - 3:390.141-3
- Fix (rfbz#5901)

* Sat Jan 16 2021 Henrik Nordstrom <henrik@henriknordstrom.net> - 390.141-2
- Re-enable nvidia-uvm. The GPL licensing issue seems to have been solved in 390.141.

* Thu Jan 07 2021 Henrik Nordstrom <henrik@henriknordstrom.net> - 3:390.141-1
- Update to 390.141

* Mon Dec 14 2020 Henrik Nordstrom <henrik@henriknordstrom.net> - 3:390.138-4
- Import patches from Debian, including kernel 5.9 support

* Thu Aug 27 2020 Leigh Scott <leigh123linux@gmail.com> - 3:390.138-3
- Patch for kernel 5.8
- Exclude nvidia-uvm due to GPL-only symbol 'radix_tree_preloads'

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3:390.138-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Leigh Scott <leigh123linux@gmail.com> - 3:390.138-1
- Update to 390.138 release

* Sun May 10 2020 Henrik Nordstrom <henrik@henriknordstrom.net> - 3:390.132-7
- Actually apply patch for kernel 5.7

* Sat May 09 2020 Henrik Nordstrom <henrik@henriknordstrom.net> - 3:390.132-6
- Patch for kernel 5.7

* Sat May 09 2020 Henrik Nordstrom <henrik@henriknordstrom.net> - 3:390.132-5
- Update kernel-5.6 patch

* Tue Mar 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 3:390.132-4.1
- Conditionlize arched patches

* Tue Mar 10 2020 Nicolas Chauvet <kwizart@gmail.com> - 3:390.132-4
- Drop armv7hl build

* Mon Mar 09 2020 Henrik Nordstrom <henrik@henriknordstrom.net> - 3:390.132-3
- Patches for kernel 5.5 and 5.6

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3:390.132-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Leigh Scott <leigh123linux@gmail.com> - 3:390.132-1
- Update to 390.132 release

* Tue Sep 03 2019 Leigh Scott <leigh123linux@gmail.com> - 3:390.129-3
- rebuilt

* Tue Sep 03 2019 Leigh Scott <leigh123linux@gmail.com> - 3:390.129-2
- Rebuild for new el7 kernel

* Tue Aug 06 2019 Leigh Scott <leigh123linux@googlemail.com> - 3:390.129-1
- Update to 390.129 release

* Sun Jun 16 2019 Leigh Scott <leigh123linux@googlemail.com> - 3:390.116-4
- Switch to Ubuntu buildfix for 5.2 kernel

* Fri May 03 2019 Leigh Scott <leigh123linux@googlemail.com> - 3:390.116-3
- Patch for 5.1rc kernel

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3:390.116-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Feb 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 3:390.116-1
- Update to 390.116 release

* Thu Jan 24 2019 Leigh Scott <leigh123linux@googlemail.com> - 3:390.87-5
- Clean up build fix for 4.20 kernel (untested)

* Mon Dec 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 3:390.87-4
- Build fix for 4.20 kernel (untested)

* Thu Oct 25 2018 Nicolas Chauvet <kwizart@gmail.com> - 3:390.87-3
- Drop obsoletes nvidia-kmod

* Wed Oct 10 2018 Leigh Scott <leigh123linux@googlemail.com> - 3:390.87-2
- Patch for 4.19 kernel

* Sun Sep 23 2018 Richard Shaw <hobbes1069@gmail.com> - 3:390.87-1
- Update to 390.87.

* Tue Jun 05 2018 Nicolas Chauvet <kwizart@gmail.com> - 3:390.67-1
- Update to 390.67
- Fork 390xx

* Wed May 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 3:390.59-1
- Update to 390.59 release

* Thu Mar 29 2018 Leigh Scott <leigh123linux@googlemail.com> - 3:390.48-1
- Update to 390.48 release

* Tue Mar 13 2018 Leigh Scott <leigh123linux@googlemail.com> - 3:390.42-1
- Update to 390.42 release

* Tue Mar 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 3:390.25-6
- Patch for 4.16 kernel

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 3:390.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 17 2018 Todd Zullinger <tmz@pobox.com> - 390.25-4
- Enable verbose make (V=1)

* Fri Feb 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 3:390.25-3
- Bump epoch to prevent cuda repo from replacing packages

* Sat Feb 10 2018 Leigh Scott <leigh123linux@googlemail.com> - 2:390.25-2
- Patch for 4.15 kernel

* Mon Jan 29 2018 Leigh Scott <leigh123linux@googlemail.com> - 2:390.25-1
- Update to 390.25 release

* Wed Jan 10 2018 Leigh Scott <leigh123linux@googlemail.com> - 2:390.12-1
- Update to 390.12 beta

* Sun Nov 26 2017 Leigh Scott <leigh123linux@googlemail.com> - 2:387.34-1
- Update to 387.34 release

* Mon Oct 30 2017 Leigh Scott <leigh123linux@googlemail.com> - 2:387.22-1
- Update to 387.22 release

* Wed Oct 04 2017 Leigh Scott <leigh123linux@googlemail.com> - 2:387.12-1
- Update to 387.12 beta

* Sat Sep 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 2:384.90-3
- revert last commit, it was caused by kernel debugging

* Sat Sep 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 2:384.90-2
- Patch for 4.13 kernel

* Thu Sep 21 2017 Leigh Scott <leigh123linux@googlemail.com> - 2:384.90-1
- Update to 384.90 release

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2:384.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Leigh Scott <leigh123linux@googlemail.com> - 2:384.59-1
- Update to 384.59 release

* Mon Jul 24 2017 Leigh Scott <leigh123linux@googlemail.com> - 2:375.82-1
- Update to 375.82 release

* Fri May 19 2017 Leigh Scott <leigh123linux@googlemail.com> - 2:375.66-3
- Drop 4.11 kernel patch, 4.11.1 kernel fixes the GPL symbols issue

* Tue May 09 2017 Leigh Scott <leigh123linux@googlemail.com> - 2:375.66-2
- Add epoch to kmod-nvidia-newest obsolete version

* Fri May 05 2017 Leigh Scott <leigh123linux@googlemail.com> - 2:375.66-1
- Update to 375.66 release

* Fri Apr 07 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:381.09-1
- Update to 381.09 beta

* Sun Mar 05 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:378.13-1
- Update to 378.13

* Mon Feb 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:375.39-2
- patch for 4.10 kernel

* Wed Feb 15 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:375.39-1
- Update to 375.39 release

* Wed Dec 14 2016 leigh scott <leigh123linux@googlemail.com> - 1:375.26-1
- Update to 375.26

* Fri Nov 18 2016 leigh scott <leigh123linux@googlemail.com> - 1:375.20-1
- Update to 375.20

* Sat Oct 22 2016 Leigh Scott <leigh123linux@googlemail.com> - 1:375.10-1
- Update to 375.10 beta release

* Fri Sep 09 2016 leigh scott <leigh123linux@googlemail.com> - 1:370.28-1
- Update to 370.28

* Fri Aug 19 2016 Leigh Scott <leigh123linux@googlemail.com> - 1:370.27-1
- Update to 370.23 beta

* Wed Aug 10 2016 leigh scott <leigh123linux@googlemail.com> - 1:367.35-2
- patch for 4.8rc kernel

* Sun Jul 17 2016 Leigh Scott <leigh123linux@googlemail.com> - 1:367.35-1
- Update to 367.35

* Fri Jul 08 2016 Leigh Scott <leigh123linux@googlemail.com> - 1:367.27-2
- patch for 4.7rc kernel

* Fri Jul 01 2016 Leigh Scott <leigh123linux@googlemail.com> - 1:367.27-1
- Update to 367.27

* Sat Nov 21 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:358.16-1
- Update to 358.16

* Fri Nov 13 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:355.11-3.4
- Rebuilt for kernel

* Fri Nov 06 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:355.11-3.3
- Rebuilt for kernel

* Tue Oct 06 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:355.11-3.2
- Rebuilt for kernel

* Wed Sep 23 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:355.11-3.1
- Rebuilt for kernel

* Wed Sep 16 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:355.11-3
- Rebuilt for kernel

* Mon Sep 14 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:355.11-2
- patch for 4.3rc kernel

* Mon Aug 31 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:355.11-1
- Update to 355.11

* Fri Aug 28 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:352.41-1
- Update to 352.41

* Fri Aug 21 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:352.30-2.4
- Rebuilt for kernel

* Thu Aug 13 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:352.30-2.3
- Rebuilt for kernel

* Fri Aug 07 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:352.30-2.2
- Rebuilt for kernel

* Thu Jul 30 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:352.30-2.1
- Rebuilt for kernel

* Wed Jul 29 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:352.30-2
- Fix build on arm - missing linux/swiotlb.h include

* Wed Jul 29 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:352.30-1
- Update to 352.30

* Fri Jul 24 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:352.21-1.4
- Rebuilt for kernel

* Mon Jun 15 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:352.21-1
- Update to 352.21

* Wed Jun 10 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.72-2.3
- Rebuilt for kernel

* Tue Jun 02 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.72-2.2
- Rebuilt for kernel

* Sun May 24 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.72-2.1
- Rebuilt for kernel

* Sun May 24 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.72-2
- Rebuilt

* Wed May 20 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:346.72-1
- Update to 343.72

* Wed May 20 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.59-1.6
- Rebuilt for kernel

* Wed May 13 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.59-1.5
- Rebuilt for kernel

* Sat May 09 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.59-1.4
- Rebuilt for kernel

* Sat May 02 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.59-1.3
- Rebuilt for kernel

* Wed Apr 22 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.59-1.2
- Rebuilt for kernel

* Wed Apr 15 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.59-1.1
- Rebuilt for kernel

* Wed Apr 08 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:346.59-1
- Update to 343.59
- drop 4.0.0 kernel patch

* Mon Mar 30 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.47-2.4
- Rebuilt for kernel

* Fri Mar 27 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.47-2.3
- Rebuilt for kernel

* Mon Mar 23 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.47-2.2
- Rebuilt for kernel

* Sat Mar 21 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.47-2.1
- Rebuilt for kernel

* Fri Mar 13 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:346.47-2
- rebuild for akmod

* Tue Mar 10 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.47-1.2
- Rebuilt for kernel

* Fri Mar 06 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.47-1.1
- Rebuilt for kernel

* Tue Feb 24 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:346.47-1
- Update to 343.47
- drop 3.18 kernel patch

* Tue Feb 24 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:346.35-2
- Patch for 4.0.0 kernel

* Sat Feb 14 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.35-1.5
- Rebuilt for kernel

* Sun Feb 08 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.35-1.4
- Rebuilt for kernel

* Wed Feb 04 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.35-1.3
- Rebuilt for kernel

* Mon Feb 02 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.35-1.2
- Rebuilt for kernel

* Wed Jan 21 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:346.35-1.1
- Rebuilt for kernel

* Fri Jan 16 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:346.35-1
- Update to 346.35

* Thu Jan 15 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:343.36-1.3
- Rebuilt for kernel

* Sat Jan 10 2015 Nicolas Chauvet <kwizart@gmail.com> - 1:343.36-1.2
- Rebuilt for kernel

* Fri Dec 19 2014 Nicolas Chauvet <kwizart@gmail.com> - 1:343.36-1.1
- Rebuilt for kernel

* Tue Dec 16 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:343.36-1
- Update to 343.36

* Sun Dec 14 2014 Nicolas Chauvet <kwizart@gmail.com> - 1:343.22-4.1
- Rebuilt for kernel

* Fri Dec 05 2014 Nicolas Chauvet <kwizart@gmail.com> - 1:343.22-4
- Rebuilt for f21 final kernel

* Tue Oct 21 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:343.22-3
- more 3.18 kernel changes

* Tue Oct 21 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:343.22-2
- Patch for 3.18 kernel

* Fri Sep 19 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:343.22-1
- Update to 343.22

* Thu Aug 07 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:343.13-1
- Update to 343.13

* Tue Jul 08 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:340.24-1
- Update to 340.24

* Tue Jun 10 2014 Nicolas Chauvet <kwizart@gmail.com> - 1:340.17-2
- Add epoch to kmodsrc requires

* Mon Jun 09 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:340.17-1
- Update to 340.17

* Thu Jun 05 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:337.25-2
- add missing requires to akmod-nvidia package

* Sat May 31 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:337.25-1
- Update to 337.25

* Sat May 17 2014 Nicolas Chauvet <kwizart@gmail.com> - 1:337.19-2
- Use kmodsrc to bundle kmod sources

* Tue May 06 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:337.19-1
- Update to 337.19

* Sat Apr 26 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:337.12-3
- remove kernel patch

* Wed Apr 09 2014 Nicolas Chauvet <kwizart@gmail.com> - 1:337.12-2
- Avoid lpae kvarriant on arm

* Tue Apr 08 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:337.12-1
- Update to 337.12

* Mon Mar 03 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:334.21-1
- Update to 334.21

* Sat Feb 08 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:334.16-1
- Update to 334.16
- Patch for 3.14 kernel

* Sat Jan 25 2014 Nicolas Chauvet <kwizart@gmail.com> - 1:331.38-5
- Disable uvm when NV_BUILD_MODULE_INSTANCES is set
- Simplify patch

* Tue Jan 21 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:331.38-4
- make more changes to 3.13 kernel patch

* Mon Jan 13 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:331.38-3
- fix patch for 3.13 kernel

* Mon Jan 13 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:331.38-2
- rebuild for akmod

* Mon Jan 13 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:331.38-1
- Update to 331.38 release
- Patch for 3.13 kernel

* Sun Dec 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:331.20-10
- Fix build with lpae kernel

* Wed Dec 11 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:331.20-9
- Resort and IGNORE XEN/RT Checks

* Tue Dec 10 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:331.20-8
- Rebuilt for f20 final kernel

* Sat Dec 07 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:331.20-7
- Rebuilt for f20 final kernel

* Sun Dec 01 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:331.20-6
- Rebuilt for f20 final kernel

* Sun Nov 24 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:331.20-5
- Bump

* Sun Nov 24 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:331.20-3
- Allow akmod to build modules for cuda
  Set %%_nv_build_module_instances 8 into /etc/rpm/cuda.dist

* Thu Nov 21 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:331.20-2.2
- Rebuilt for kernel

* Thu Nov 14 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:331.20-2.1
- Rebuilt for kernel

* Mon Nov 11 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:331.20-2
- Add nvidia-uvm
- Fix build directory layout - rfbz#2907

* Thu Nov 07 2013 Leigh Scott <leigh123linux@googlemail.com> - 1:331.20-1
- Update to 331.20 release

* Wed Nov 06 2013 Leigh Scott <leigh123linux@googlemail.com> - 1:325.15-4
- use nvidia fix for get_num_physpages

* Mon Sep 16 2013 Leigh Scott <leigh123linux@googlemail.com> - 1:325.15-3
- patch for 3.12 git kernel

* Tue Aug 06 2013 Leigh Scott <leigh123linux@googlemail.com> - 1:325.15-2
- rebuild for akmod as pae marco is broken

* Tue Aug 06 2013 Leigh Scott <leigh123linux@googlemail.com> - 1:325.15-1
- Update to 325.15 release
- redo kernel patch

* Sun Jul 21 2013 Leigh Scott <leigh123linux@googlemail.com> - 1:325.08-4
- redo kernel patch

* Tue Jul 16 2013 leigh scott <leigh123linux@googlemail.com> - 1:325.08-3
- add better patch for 3.10 and 3.11 git kernels

* Mon Jul 08 2013 leigh scott <leigh123linux@googlemail.com> - 1:325.08-2
- build for current

* Sun Jul 07 2013 leigh scott <leigh123linux@googlemail.com> - 1:325.08-1
- Update to 325.08

* Fri Jun 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:319.32-1
- Update to 319.32
- Add support for armv7hl

* Fri May 31 2013 leigh scott <leigh123linux@googlemail.com> - 1:319.23-3
- Patch for 3.10 kernel

* Thu May 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:319.23-2
- Build for akmods

* Thu May 23 2013 Leigh Scott <leigh123linux@googlemail.com> - 1:319.23-1
- Update to 319.23

* Sat May 11 2013 Leigh Scott <leigh123linux@googlemail.com> - 1:319.17-1
- Update to 319.17

* Wed May 01 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:319.12-1
- Update to 319.12

* Mon Apr 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:313.30-2
- Build for kernel akmods

* Thu Apr 04 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:313.30-1
- Update to 313.30

* Sun Feb 17 2013 Leigh Scott <leigh123linux@googlemail.com> - 1:313.18-2
- Fix with a better patch from gentoo

* Wed Jan 16 2013 Leigh Scott <leigh123linux@googlemail.com> - 1:313.18-1
- Update to 313.18 (adds xorg-server 1.14 ABI support)
- patch for 3.8rc kernel

* Fri Nov 16 2012 Leigh Scott <leigh123linux@googlemail.com> - 1:310.19-1
- rebuilt

* Tue Oct 16 2012 Leigh Scott <leigh123linux@googlemail.com> - 1:310.14-2
- add patch for 3.7rc kernel

* Tue Oct 16 2012 Leigh Scott <leigh123linux@googlemail.com> - 1:310.14-1
- Update to 310.14

* Mon Sep 24 2012 Leigh Scott <leigh123linux@googlemail.com> - 1:304.51-1
- Update to 304.51

* Sat Sep 15 2012 Leigh Scott <leigh123linux@googlemail.com> - 1:304.48-1
- Update to 304.48

* Wed Sep 05 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:304.43-1
- Update to 304.43

* Tue Aug 14 2012 Leigh Scott <leigh123linux@googlemail.com> - 1:304.37-1
- Update to 304.37 release

* Sat Aug 04 2012 Leigh Scott <leigh123linux@googlemail.com> - 1:304.32-2
- build again as the build system lost the first one

* Sat Aug 04 2012 Leigh Scott <leigh123linux@googlemail.com> - 1:304.32-1
- Update to 304.32

* Tue Jul 31 2012 Leigh Scott <leigh123linux@googlemail.com> - 1:304.30-2
- add some conditionals to the 3.6 kernel patch

* Tue Jul 31 2012 Leigh Scott <leigh123linux@googlemail.com> - 1:304.30-1
- Update to 304.30

* Fri Jul 13 2012 Leigh Scott <leigh123linux@googlemail.com> - 1:304.22-1
- Update to 304.22

* Sat Jun 16 2012 leigh scott <leigh123linux@googlemail.com> - 1:302.17-1
- Update to 302.17

* Tue May 22 2012 leigh scott <leigh123linux@googlemail.com> - 1:302.11-1
- Update to 302.11

* Tue May 22 2012 leigh scott <leigh123linux@googlemail.com> - 1:295.53-1
- Update to 295.53

* Sun May 13 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:295.49-1.4
- Rebuilt for release kernel

* Wed May 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:295.49-1.3
- rebuild for updated kernel

* Sun May 06 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:295.49-1.2
- rebuild for updated kernel

* Sat May 05 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:295.49-1.1
- rebuild for updated kernel

* Thu May 03 2012 leigh scott <leigh123linux@googlemail.com> - 1:295.49-1
- Update to 295.49

* Wed May 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:295.40-1.5
- rebuild for updated kernel

* Sat Apr 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:295.40-1.4
- rebuild for updated kernel

* Sun Apr 22 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:295.40-1.3
- rebuild for updated kernel

* Mon Apr 16 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:295.40-1.2
- rebuild for updated kernel

* Thu Apr 12 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:295.40-1.1
- rebuild for beta kernel

* Wed Apr 11 2012 leigh scott <leigh123linux@googlemail.com> - 1:295.40-1
- Update to 295.40

* Thu Mar 22 2012 leigh scott <leigh123linux@googlemail.com> - 1:295.33-1
- Update to 295.33

* Thu Mar 22 2012 leigh scott <leigh123linux@googlemail.com> - 1:295.20-2
- patched to build with 3.3.0 kernel

* Tue Feb 14 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:295.20-1
- Update to 295.20

* Tue Feb 07 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:295.17-1.1
- Rebuild for UsrMove

* Wed Feb 01 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:295.17-1
- Update to 295.17 (beta)

* Sat Dec 31 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:295.09-1
- Update to 295.09 (beta)

* Tue Nov 22 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:290.10-1
- Update to 290.10

* Wed Nov 09 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:290.06-1
- Update to 290.06 beta

* Wed Nov 02 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:285.05.09-1.4
- Rebuild for F-16 kernel

* Tue Nov 01 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:285.05.09-1.3
- Rebuild for F-16 kernel

* Fri Oct 28 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:285.05.09-1.2
- Rebuild for F-16 kernel

* Sun Oct 23 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:285.05.09-1.1
- Rebuild for F-16 kernel

* Tue Oct 04 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:285.05.09-1
- Update to 285.05.09

* Sat Aug 27 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:285.03-1
- Update to 285.03
- Remove kernel-xen filter

* Tue Aug 02 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:280.13-2
- Update to 280.13

* Sun Jul 24 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:280.11-1
- Update to 280.11

* Fri Jul 01 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:280.04-1
- Update to 280.04 (beta)

* Tue Jun 14 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:275.09.07-1
- Update to 275.09.07

* Wed Jun 08 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:270.41.19-1
- Update to 270.41.19

* Sat Apr 30 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:270.41.06-1
- Update to 270.41.06

* Tue Apr 12 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:270.41.03-1
- Update to 270.41.03

* Thu Mar 03 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:270.30-1
- Update to 270.30

* Tue Mar 01 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:270.29-1
- Update to 270.29

* Sun Jan 23 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:270.18-1
- Update to 270.18 beta

* Fri Jan 21 2011 Nicolas Chauvet <kwizart@gmail.com> - 1:260.19.36-1
- Update to 260.19.36

* Tue Dec 14 2010 Nicolas Chauvet <kwizart@gmail.com> - 1:260.19.29-1
- Update to 260.19.29

* Thu Nov 11 2010 Nicolas Chauvet <kwizart@gmail.com> - 1:260.19.21-1
- Update to 260.19.21

* Thu Oct 14 2010 Nicolas Chauvet <kwizart@gmail.com> - 1:260.19.12-1
- Update to 260.19.12

* Thu Oct 07 2010 Nicolas Chauvet <kwizart@gmail.com> - 1:260.19.06-1
- Update to 260.19.06 beta

* Wed Sep 01 2010 Nicolas Chauvet <kwizart@gmail.com> - 1:256.53-1
- Update to 256.53

* Thu Aug 05 2010 Nicolas Chauvet <kwizart@gmail.com> - 1:256.44-1
- Update to 256.44

* Fri Jun 18 2010 Vallimar de Morieve <vallimar@gmail.com> - 1:256.35-1
- update to 256.35

* Thu Jun 17 2010 Nicolas Chaubvet <kwizart@gmail.com> - 1:195.36.31-1
- Update to 195.36.31
- Fix acpi_walk_namespace call with kernel 2.6.33 and later.
  http://bugs.gentoo.org/show_bug.cgi?id=301318

* Sun Jun 13 2010 Nicolas Chauvet <kwizart@gmail.com> - 1:195.36.24-2
- Backport IOMMU - http://www.nvnews.net/vbulletin/showthread.php?t=151791

* Sat Apr 24 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1:195.36.24-1
- Update to 195.36.24

* Sat Mar 27 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1:195.36.15-1
- Update to 195.36.15

* Fri Mar 12 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1:190.53-3
- Bump Epoch - Fan problem in recent release

* Mon Mar 08 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 1:190.53-2
- Revert to 190.53 version
  http://www.nvnews.net/vbulletin/announcement.php?f=14

* Sat Feb 27 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 195.36.08-1
- Update to 195.36.08

* Sat Feb 20 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.53-1.6
- rebuild for new kernel

* Sat Feb 20 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.53-1.5
- rebuild for new kernel

* Thu Feb 11 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.53-1.4
- rebuild for new kernel

* Wed Feb 10 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.53-1.3
- rebuild for new kernel

* Sat Jan 30 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.53-1.2
- rebuild for new kernel

* Wed Jan 20 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.53-1.1
- rebuild for new kernel

* Wed Dec 30 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 190.53-1
- Update to 190.53
- Add patch for VGA_ARB

* Sat Dec 26 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.42-1.9
- rebuild for new kernel

* Thu Dec 10 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.42-1.8
- rebuild for new kernel

* Sun Dec 06 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.42-1.7
- rebuild for new kernel

* Wed Nov 25 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.42-1.6
- rebuild for new kernel

* Sun Nov 22 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.42-1.5
- rebuild for new kernel, disable i586 builds

* Tue Nov 10 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.42-1.4
- rebuild for F12 release kernel

* Mon Nov 09 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.42-1.3
- rebuild for new kernels

* Fri Nov 06 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.42-1.2
- rebuild for new kernels

* Wed Nov 04 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 190.42-1.1
- rebuild for new kernels

* Sat Oct 31 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 190.42-1
- Update to 190.42

* Tue Oct 20 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 185.18.36-1.3
- rebuild for new kernels

* Wed Sep 30 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 185.18.36-1.2
- rebuild for new kernels

* Tue Sep 01 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 185.18.36-1.1
- rebuild for new kernels

* Sat Aug 29 2009 kwizart < kwizart at gmail.com > - 185.18.36-1
- Update to 185.18.36 (final)

* Thu Aug 27 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 185.18.14-1.8
- rebuild for new kernels

* Sun Aug 23 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 185.18.14-1.7
- rebuild for new kernels

* Sat Aug 22 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 185.18.14-1.6
- rebuild for new kernels

* Sat Aug 15 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 185.18.14-1.5
- rebuild for new kernels

* Fri Aug 14 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 185.18.14-1.4
- rebuild for new kernels

* Fri Aug  7 2009 kwizart < kwizart at gmail.com > - 185.18.14-1.3
- Revert to 185.18.14
- rebuild for new kernels

* Tue Jul 14 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 185.18.14-1.2
- rebuild for new kernels

* Mon Jun 22 2009 kwizart < kwizart at gmail.com > - 185.18.14-1.1
- rebuild for new kernels

* Fri Jun  5 2009 kwizart < kwizart at gmail.com > - 185.18.14-1
- Update to 185.18.14 (final)

* Fri Jun 05 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.51-1.8
- rebuild for final F11 kernel

* Thu May 28 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.51-1.7
- rebuild for new kernels

* Wed May 27 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.51-1.6
- rebuild for new kernels

* Thu May 21 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.51-1.5
- rebuild for new kernels

* Wed May 13 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.51-1.4
- rebuild for new kernels

* Tue May 05 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.51-1.3
- rebuild for new kernels

* Sat May 02 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.51-1.2
- rebuild for new kernels

* Sun Apr 26 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.51-1.1
- rebuild for new kernels

* Wed Apr 22 2009 kwizart < kwizart at gmail.com > - 180.51-1
- Update to 180.51 (stable)
- Don't Obsoletes the beta serie anymore (only the newest)

* Sun Apr 05 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.37-2.1
- rebuild for new kernels

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.37-2
- rebuild for new F11 features

* Mon Mar  9 2009 kwizart < kwizart at gmail.com > - 180.37-1
- Update to 180.37 (prerelease)

* Thu Feb 26 2009 kwizart < kwizart at gmail.com > - 180.35-2
- Handle Obsoletes/Provides in nvidia-kmod for nvidia-beta-kmod

* Wed Feb 25 2009 kwizart < kwizart at gmail.com > - 180.35-1
- Update to 180.35 (prerelease)

* Sun Feb 15 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.29-1.1
- rebuild for latest Fedora kernel;

* Tue Feb 10 2009 kwizart < kwizart at gmail.com > - 180.29-1
- Update to 180.29 (stable)
- Reintroduce build for i586 since it will match for SSE without PAE CPU.
 (remember that nvidia main series needs SSE capable CPU).
- Empty the xen exclusion filter.

* Sun Feb 01 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.27-1.1
- rebuild for latest Fedora kernel;

* Thu Jan 29 2009 kwizart < kwizart at gmail.com > - 180.27-1
- Update to 180.27 (beta)

* Tue Jan 27 2009 kwizart < kwizart at gmail.com > - 180.25-1
- Update to 180.25 (beta)

* Sun Jan 25 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.22-1.3
- rebuild for latest Fedora kernel;

* Sun Jan 18 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.22-1.2
- rebuild for latest Fedora kernel;

* Sun Jan 11 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.22-1.1
- rebuild for latest Fedora kernel;

* Thu Jan  8 2009 kwizart < kwizart at gmail.com > - 180.22-1
- Update to 180.22 (stable)

* Sun Jan 04 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.18-1.2
- rebuild for latest Fedora kernel;

* Sun Dec 28 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.18-1.1
- rebuild for latest Fedora kernel;

* Sun Dec 28 2008 kwizart < kwizart at gmail.com > - 180.18-1
- Update to 180.18 (beta)

* Sun Dec 21 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 180.16-1.1
- rebuild for latest Fedora kernel;

* Wed Dec 17 2008 kwizart < kwizart at gmail.com > - 180.16-1
- Update to 180.16

* Sun Dec 14 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 177.82-1.5
- rebuild for latest Fedora kernel;

* Sat Nov 22 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 177.82-1.4
- rebuilt

* Sat Nov 22 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 177.82-1.3
- rebuild for latest Fedora kernel;

* Wed Nov 19 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 177.82-1.2
- rebuild for latest Fedora kernel;

* Tue Nov 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 177.82-1.1
- rebuild for latest Fedora kernel;

* Thu Nov 13 2008 kwizart < kwizart at gmail.com > - 177.82-1
- Update to 177.82

* Sun Nov 09 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 177.80-1.4
- rebuild for latest Fedora kernel;

* Sun Nov 02 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 177.80-1.3
- rebuild for latest rawhide kernel;

* Sun Oct 26 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 177.80-1.2
- rebuild for latest rawhide kernel

* Sun Oct 19 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 177.80-1.1
- rebuild for latest rawhide kernel

* Mon Oct 13 2008 kwizart < kwizart at gmail.com > - 177.80-1
- Update to 177.80

* Sun Oct 5 2008 Stewart Adam <s.adam at diffingo.com> - 177.78-3
- Disable EXTRA_LDFLAGS in patches

* Sun Oct 05 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 177.78-2.1
- rebuild for rpm fusion

* Wed Oct 1 2008 Stewart Adam < s.adam at diffingo.com > - 177.78-1
- Update to 177.78 beta

* Mon Sep 15 2008 Stewart Adam < s.adam at diffingo.com > - 177.70-1
- Update to 177.70
- Skip all Xen sanity checks

* Thu Jul 31 2008 kwizart < kwizart at gmail.com > - 173.14.12-1
- Update to 173.14.12

* Tue Jun 17 2008 kwizart < kwizart at gmail.com > - 173.14.09-1
- Update to 173.14.09
- Remove i586 (driver needs CPU to have SSE)

* Wed May 28 2008 kwizart < kwizart at gmail.com > - 173.14.05-2
- Add NVIDIA_kernel-173.14.05-2419292.diff.txt

* Wed May 28 2008 kwizart < kwizart at gmail.com > - 173.14.05-1
- Update to 173.14.05

* Thu Apr 10 2008 kwizart < kwizart at gmail.com > - 173.08-1
- Update to 173.08 (beta) - Fedora 9 experimental support
  See: http://www.nvnews.net/vbulletin/showthread.php?t=111460

* Wed Mar 19 2008 kwizart < kwizart at gmail.com > - 171.06-2
- Add Patch for 2.6.25rc kernels

* Sat Mar  8 2008 kwizart < kwizart at gmail.com > - 171.06-1
- Update to 171.06 (beta)

* Wed Feb 27 2008 kwizart < kwizart at gmail.com > - 169.12-1
- Update to 169.12

* Sun Feb  3 2008 kwizart < kwizart at gmail.com > - 169.09-5
- typo fixes

* Sat Feb  2 2008 kwizart < kwizart at gmail.com > - 169.09-3
- Reenable debuginfo
- Disable xen check properly (still not working)
- Remove the smbus patch (uneeded).

* Sat Jan 26 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 169.09-2
- rebuild for new kmodtools, akmod adjustments

* Wed Jan 23 2008 Stewart Adam <s.adam AT diffingo DOT com> - 169.09-1
- Update to 169.09
- Fix License tag

* Sun Jan 20 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 169.07-2
- build akmods package

* Sat Dec 22 2007 Stewart Adam < s.adam AT diffingo DOT com > - 169.07-1
- Update to 169.07
- Don't build debug to fix BuildID error

* Mon Nov 05 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 100.14.19-17
- rebuilt for F8 kernels

* Wed Oct 31 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 100.14.19-16
- rebuilt for latest kernels

* Tue Oct 30 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 100.14.19-15
- rebuilt for latest kernels

* Sun Oct 28 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 100.14.19-14
- rebuilt for latest kernels
- adjust to rpmfusion and new kmodtool

* Sat Oct 27 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 100.14.19-13
- rebuilt for latest kernels

* Tue Oct 23 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 100.14.19-12
- rebuilt for latest kernels

* Mon Oct 22 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 100.14.19-11
- rebuilt for latest kernels

* Thu Oct 18 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 100.14.19-10
- rebuilt for latest kernels

* Thu Oct 18 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 100.14.19-9
- rebuilt for latest kernels

* Fri Oct 12 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 100.14.19-8
- rebuilt for latest kernels

* Thu Oct 11 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 100.14.19-7
- rebuilt for latest kernels

* Wed Oct 10 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 100.14.19-6
- rebuilt for latest kernels

* Tue Oct 09 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> 100.14.19-5
- rebuilt for latest kernels

* Sun Oct 07 2007 Thorsten Leemhuis <fedora AT leemhuis DOT info>
- build for rawhide kernels as of today

* Thu Oct 04 2007 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 100.14.19-3
- fix typo

* Wed Oct 03 2007 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 100.14.19-2
- update for new kmod-helper stuff
- build for newest kernels

* Thu Sep 20 2007 kwizart < kwizart at gmail.com > - 100.14.19-1
- Update to Final 100.14.19

* Sun Sep 09 2007 Thorsten Leemhuis < fedora AT leemhuis DOT info > - 100.14.11-4
- Build for latest only

* Sun Sep 09 2007 Thorsten Leemhuis < fedora AT leemhuis DOT info > - 100.14.11-3
- Convert to new kmods stuff from livna
- Rebuild for F8T2 and rawhide

* Fri Aug 10 2007 Stewart Adam < s.adam AT diffingo DOT com > - 100.14.11-2
- Add patch from nvnews for 2.6.23rc2 support
- Rebuild for F8T1

* Thu Jun 21 2007 Stewart Adam < s.adam AT diffingo DOT com > - 100.14.11-1
- Update to 100.14.11
- Drop unneeded patches

* Sun Jun 10 2007 kwizart < kwizart at gmail.com > - 100.14.09-1
- Update to Final 100.14.09

* Sun May 27 2007 kwizart < kwizart at gmail.com > - 1.0.9762-1
- Update to 1.0.9762

* Fri Apr 27 2007 Stewart Adam < s.adam AT diffingo DOT com > - 1.0.9755-3
- Rebuild for F7T4 (fixed kversion)
- Fix changelog dates

* Fri Apr 27 2007 kwizart < kwizart at gmail.com > - 1.0.9755-2
- Build for Fedora test4 kernel

* Thu Mar 8 2007 kwizart < kwizart at gmail.com > - 1.0.9755-1
- Update to 1.0.9755
- Build to current 2.6.20-1.2967.fc7

* Sun Mar 4 2007 Stewart Adam < s.adam AT diffingo DOT com > - 1.0.9746-7
- kdump for non-i686
- Fix dates in changelog

* Sat Mar 3 2007 Stewart Adam < s.adam AT diffingo DOT com > - 1.0.9746-6
- No kdump
- New kernel

* Fri Mar 2 2007 Stewart Adam < s.adam AT diffingo DOT com > - 1.0.9746-5
- New kernel
- Make Source0 a URL

* Sat Feb 24 2007 Stewart Adam < s.adam AT diffingo DOT com > - 1.0.9746-4
- Standardize all summaries and descriptions with other nvidia and fglrx
  packages
- Move paths from nvidia-glx to nvidia

* Wed Feb 7 2007 kwizart < kwizar at gmail.com > - 1.0.9746-3
- Disable xen variant

* Wed Feb 7 2007 kwizart < kwizar at gmail.com > - 1.0.9746-2
- Rebuild for Fedora Core 7 test1

* Tue Dec 26 2006 kwizart < kwizart at gmail.com > - 1.0.9746-1
- Update to release 1.0.9746 (Final).
- Standard version do not support xen kernel.
- Update xen patch: patch-nv-1.0-9625-xenrt.txt

* Thu Nov 23 2006 Stewart Adam < s.adam AT diffingo DOT com > - 1.0.9742-2
- Change %%description, as NV30 and below no longer supported
- Update nvidia desktop file

* Mon Nov 20 2006 kwizart < kwiart at gmail.com > - 1.0.9742-1
- Update to release 1.0.9742

* Tue Nov 07 2006 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 1.0.9629-1
- update to release 1.0.9629
- include xen patch (thx to Bob Richmond)

* Wed Nov 01 2006 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 1.0.9626-2
- include patch from
  http://www.nvnews.net/vbulletin/showpost.php?p=996233&postcount=20

* Sun Oct 22 2006 Stewart Adam <s.adam AT diffingo DOT com> - 1.0.9626-1
- update to release 1.0.9626

* Sat Oct 07 2006 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 1.0.8774-2
- sed-away the config.h include

* Thu Aug 24 2006 Niko Mirthes (straw) <nmirthes AT gmail DOT com> - 1.0.8774-1
- update to release 1.0.8774

* Thu Aug 10 2006 Niko Mirthes (straw) <nmirthes AT gmail DOT com> - 1.0.8762-5
- update for kernel 2.6.17-1.2174_FC5

* Mon Aug 07 2006 Niko Mirthes (straw) <nmirthes AT gmail DOT com> - 1.0.8762-4
- forgot to update release field

* Fri Aug 04 2006 Niko Mirthes (straw) <nmirthes AT gmail DOT com> - 1.0.8762-3
- minor changes to spacing, removal of random tabs, re-arrangements

* Sun Jun 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0.8762-2
- Invoke kmodtool with bash instead of sh.

* Wed May 24 2006 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 1.0.8762-1
- update to 1.0.8762

* Sun May 14 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0.8756-3
- Require version >= of nvidia-kmod-common.
- Provide nvidia-kmod instead of kmod-nvidia to fix upgrade woes (#970).

* Thu Apr 27 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0.8756-2
- Provide "kernel-modules" instead of "kernel-module" to match yum's config.

* Sat Apr 08 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.0.8756-1
- Update to 8756
- drop patch

* Thu Mar 23 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.0.8178-6
- disable xen0 for now

* Wed Mar 22 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.0.8178-5
- build for 2.6.16-1.2069_FC5

* Wed Mar 22 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.0.8178-4
- allow to pass kversion and kvariants via command line

* Sat Mar 18 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.0.8178-3
- drop 0.lvn
- use kmodtool from svn
- hardcode kernel and variants

* Mon Jan 30 2006 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 1.0.8178-0.lvn.2
- Some minor fixes
- new kmodtool

* Sun Jan 22 2006 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 1.0.8178-0.lvn.1
- split into packages for userland and kmod
- rename to nvidia-kmod

* Thu Dec 22 2005 Niko Mirthes (straw) <nmirthes AT gmail DOT com> - 0:1.0.8178-0.lvn.2
- change nvidia-glx.sh and nvidia-glx.csh to point to README.txt rather than README
- reference xorg.conf rather than XF86Config in the init script
- improve readability of instructions and comments, fix some typos
- drop epoch, as it seems to be affecting dependencies according to rpmlint
- tweak the nvidia-settings desktop file so it always shows up on the
  menu in the right location
- add the manual pages for nvidia-settings and nvidia-xconfig
- remove header entries from the nvidia-glx files list. they belong in -devel
- fix changelog entries to refer to 7676 not 7176 (though there was a 7176 x86_64
  release prior to 7174)
- add libXvMCNVIDIA.so
- update to 8178

* Wed Dec 07 2005 Niko Mirthes (straw) <nmirthes AT gmail DOT com> - 0:1.0.8174-0.lvn.1
- add the manual pages for nvidia-settings and nvidia-xconfig
- install the new nvidia-xconfig utility and associated libs

* Mon Dec 05 2005 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 0:1.0.8174-0.lvn.1
- Update to 8174
- desktop entry now Categories=Settings (#665)
- Ship bug-reporting tool in doc (#588)
- Things from Bug 635, Niko Mirthes (straw) <nmirthes AT gmail DOT com>:
-- avoid changing time stamps on libs where possible
-- only add /etc/modprobe.conf entries if they aren't already there
-- add /etc/modprobe.conf entries one at a time
-- only remove /etc/modprobe.conf entries at uninstall, not during upgrade
-- avoid removing any modprobe.conf entries other than our own
-- match Xorg's install defaults where it makes sense (0444)
-- a few other minor tweaks to the files lists

* Sun Sep 04 2005 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 0:1.0.7676-0.lvn.3
- Conflics with nvidia-glx-legacy
- Integrate some minor correction suggested by Niko Mirthes
  <nmirthes AT gmail DOT com> in #475

* Fri Aug 26 2005 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 0:1.0.7676-0.lvn.2
- Rename src5: nvidia.init to nvidia-glx-init
- Fix correct servicename in nvidia-glx-init
- Run nvidia-glx-init before gdm-early-login; del and readd the script
  during post

* Sun Aug 21 2005 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 0:1.0.7676-0.lvn.1
- Update to 7676
- Lots of cleanup from me and Niko Mirthes <nmirthes AT gmail DOT com>
- add NVreg_ModifyDeviceFiles=0 to modprobe.conf (Niko)
- Drop support for FC2
- Nearly proper Udev-Support with workarounds around FC-Bug 151527

* Fri Jun 17 2005 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.7174-0.lvn.5
- Slight change of modprobe.conf rexexp

* Thu Jun 16 2005 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.7174-0.lvn.4
- Fixed a critical bug in modprobe.conf editing where all lines starting with alias and
  ending with then a word starting with any of the letters n,v,i,d,i,a,N,V,r,e is removed.

* Mon Jun 13 2005 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 0:1.0.7174-0.lvn.3
- Adjust kenrnel-module-stuff for FC4
- Ship both x86 and x64 in the SRPM

* Sun Jun 12 2005 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.7174-0.lvn.2
- Only create 16 devices
- Put libXvMCNVIDIA.a in -devel
- Don't remove nvidia options in /etc/modprobe.conf
- Make ld.so.conf file config(noreplace)
- Use same directory permissions as the kernel

* Sat Apr 2 2005 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.7174-0.lvn.1
- New upstream release, 7174

* Wed Mar 30 2005 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.7167-0.lvn.5
- Added x86_64 support patch from Thorsten Leemhuis

* Wed Mar 23 2005 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.7167-0.lvn.4
- Fix kernel module permissions again (644)
- Only create 16 /dev/nvidia* devices, 256 is unnecessary

* Fri Mar 18 2005 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.7167-0.lvn.3
- Fixed kernel-module permissions

* Thu Mar 17 2005 Dams <anvil[AT]livna.org> 0:1.0.7167-0.lvn.2
- Removed provides on kernel-module and kernel-modules

* Sat Mar 05 2005 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.7167-0.lvn.1
- New upstream release 1.0.7167
- Added patch from http://www.nvnews.net/vbulletin/showthread.php?t=47405
- Removed old patch against 2.6.9

* Sat Feb 05 2005 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6629-0.lvn.7
- Added a number of post-6629 patches from http://www.minion.de/files/1.0-6629
- Fixed permissions of nvidia/nvidia.ko

* Fri Jan 21 2005 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6629-0.lvn.6
- Fix incorrect MAKDEV behaviour and dependency

* Tue Nov 30 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6629-0.lvn.4
- Fixed creation of /dev/nvidia* on FC2

* Sat Nov 27 2004 Dams <anvil[AT]livna.org> - 0:1.0.6629-0.lvn.3
- Dont try to print kvariant in description when it's not defined.

* Sun Nov 21 2004 Thorsten Leemhuis <fedora at leemhuis dot info> - 0:1.0.6629-0.lvn.2
- resulting kernel-module package now depends again on /root/vmlinuz-<kernelver>
- Use rpmbuildtags driverp and kernelp

* Sat Nov 06 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6629-0.lvn.1
- New upstream version, 1.0-6629
- Build without kernel-module-devel by default

* Fri Oct 29 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6111-0.lvn.6
- Make n-c-display handle misc problems in a better way
- Fixed wrong icon file name in .desktop file
- Re-added the mysteriously vanished sleep line in the init script
  when kernel module wasn't present

* Fri Oct 22 2004 Thorsten Leemhuis <fedora at leemhuis dot info> - 0:1.0.6111-0.lvn.5
- Use fedora-kmodhelper in the way ntfs or ati-fglrx use it
- Allow rpm to strip the kernel module. Does not safe that much space ATM but
  might be a good idea
- Allow to build driver and kernel-module packages independent of each other
- Some minor spec-file changes

* Thu Oct 21 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6111-0.lvn.4
- udev fixes
- Incorporated fix for missing include line in ld.so.conf from ati-fglrx spec (T Leemhuis)

* Sun Sep 19 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6111-0.lvn.3
- Remove FC1/kernel 2.4 compability
- Rename srpm to nvidia-glx
- Build with kernel-module-devel

* Sun Aug 15 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6111-0.lvn.2
- Restore ldsoconfd macro
- Disable autoamtic removal of scripted installation for now; needs testing

* Sat Aug 14 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6111-0.lvn.1
- Upstream release 6111
- Fixed init script (again)

* Tue Aug  3 2004 Dams <anvil[AT]livna.org> 0:1.0.6106-0.lvn.4
- ld.so.conf.d directory detected by spec file
- Using nvidialibdir in nvidia-glx-devel files section
- Got rid of yarrow and tettnang macros
- libGL.so.1 symlink in tls directory always present

* Mon Jul 19 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6106-0.lvn.3
- Fixed script bug that would empty prelink.conf
- Added symlink to non-tls libGL.so.1 on FC1

* Tue Jul 13 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6106-0.lvn.2.3
- Updated init script to reflect name change -xfree86 -> -display

* Mon Jul 12 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6106-0.lvn.2.2
- Fixed backup file naming

* Sun Jul 11 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6106-0.lvn.2.1
- Restore working macros
- Always package the gui tool

* Sun Jul 11 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6106-0.lvn.2
- Renamed nvidia-config-xfree86 to nvidia-config-display
- Fixed symlinks
- Use ld.so.conf.d on FC2
- Remove script installation in pre
- Use system-config-display icon for nvidia-settings
- 2 second delay in init script when kernel module not found
- Make nvidia-config-display fail more gracefully
- Add blacklist entry to prelink.conf on FC1

* Mon Jul 05 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.6106-0.lvn.1
- New upstream release
- First attempt to support FC2
- Dropped dependency on XFree86

* Mon Feb 09 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.5336-0.lvn.3
- Use pkg0

* Sun Feb 08 2004 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.5336-0.lvn.2
- New Makefile variable SYSSRC to point to kernel sources.
- kmodhelper fixes.

* Fri Jan 30 2004 Keith G. Robertson-Turner <nvidia-devel[AT]genesis-x.nildram.co.uk> 0:1.0.5336-0.lvn.1
- New upstream release
- Removed (now obsolete) kernel-2.6 patch
- Install target changed upstream, from "nvidia.o" to "module"
- Linked nv/Makefile.kbuild to (now missing) nv/Makefile

* Sun Jan 25 2004 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.18
- Updated nvidia-config-display
- Now requiring pyxf86config

* Mon Jan 19 2004 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.17
- Added nvidiasettings macro to enable/disable gui packaging

* Mon Jan 19 2004 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.16
- Updated minion.de patches
- Added some explicit requires
- Test nvidia-config-xfree86 presence in kernel-module package
  scriptlets

* Mon Jan 12 2004 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.15
- Updated Readme.fedora
- nvidia-glx-devel package

* Sat Jan  3 2004 Dams <anvil[AT]livna.org> 0:1.0.5328-0.lvn.14
- Hopefully fixed kernel variant thingy

* Fri Jan  2 2004 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.13
- Support for other kernel variants (bigmem, etc..)
- Changed URL in Source0

* Tue Dec 30 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.13
- Dropped nvidia pkgX information in release tag.

* Tue Dec 30 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.12.pkg0
- Renamed kernel module package in a kernel-module-nvidia-`uname -r` way
- Using fedora.us kmodhelper for kernel macro
- Using nvidia pkg0 archive

* Sun Dec 21 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.11.pkg1
- kernel-module-nvidia package provides kernel-module
- We wont own devices anymore. And we wont re-create them if they are
  already present

* Sun Dec 21 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.10.pkg1
- Yet another initscript update. Really.
- Scriptlets updated too

* Sun Dec 21 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.9.pkg1
- Fixed alias in modprobe.conf for 2.6

* Sun Dec 21 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.8.pkg1
- Another initscript update

* Sun Dec 21 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.7.pkg1
- kernel module requires kernel same kversion
- initscript updated again
- Dont conflict, nor obsolete XFree86-Mesa-libGL. Using ld.so.conf to
  make libGL from nvidia first found. Hope Mike Harris will appreciate.

* Sun Dec 21 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.6.pkg1
- kernel-module-nvidia requires kernel same version-release

* Sat Dec 20 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.6.pkg1
- Updated initscript

* Fri Dec 19 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.lvn.5.pkg1
- lvn repository tag

* Fri Dec 19 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.fdr.5.pkg1
- Added initscript to toggle nvidia driver according to running kernel
  and installed kernel-module-nvidia packages
- Updated scriptlets

* Thu Dec 18 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.fdr.4.pkg1
- Arch detection
- Url in patch0

* Tue Dec 16 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.fdr.3.pkg1
- Desktop entry for nvidia-settings
- s/kernel-module-{name}/kernel-module-nvidia
- nvidia-glx doesnt requires kernel-module-nvidia-driver anymore
- Using modprobe.conf for 2.6 kernel
- Hopefully fixed symlinks

* Mon Dec 15 2003 Dams <anvil[AT]livna.org> 0:1.0.4620-0.fdr.2.pkg1
- Building kernel module for defined kernel
- kernel module for 2.6 is nvidia.ko
- Patch not to install kernel module on make install
- Updated patch for 2.6
- depmod in scriptlet for defined kernel
- nvidia-glx conflicting XFree86-Mesa-libGL because we 0wn all its
  symlink now
- Dont override libGL.so symlink because it belongs to XFree86-devel
- Added nvidia 'pkgfoo' info to packages release
- Spec file cleanup

* Fri Dec 12 2003 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.4620-0.fdr.2
- Fixed repairing of a link in post-uninstall
- Obsolete Mesa instead of Conflict with it, enables automatic removal.

* Mon Dec 08 2003 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.4620-0.fdr.1
- Added support for 2.6 kernels
- Cleaned up build section, removed the need for patching Makefiles.
- Added missing BuildReq gcc32
- Don't package libs twice, only in /usr/lib/tls/nvidia
- Made config cript executable and put it into /usr/sbin
- Moved kernel module to kernel/drivers/video/nvidia/
- Fixed libGL.so and libGLcore.so.1 links to allow linking against OpenGL libraries

* Mon Dec 08 2003 Keith G. Robertson-Turner <nvidia-devel at genesis-x.nildram.co.uk> - 0:1.0.4620-0.fdr.0
- New beta 4620 driver
- New GUI control panel
- Some minor fixes

* Thu Nov 20 2003 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.4496-0.fdr.10.1
- Finally fixed SMP builds.

* Wed Nov 19 2003 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.4496-0.fdr.9
- Don't make nvidia-glx depend on kernel-smp

* Tue Nov 18 2003 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.4496-0.fdr.8
- Some build fixes

* Tue Nov 11 2003 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.4496-0.fdr.7
- Added CC=gcc32
- Fixed upgrading issue
- Added driver switching capabilities to config script.

* Fri Nov 07 2003 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.4496-0.fdr.4
- Added conflict with XFree86-Mesa-libGL.
- Disabled showing of the README.Fedora after installation.

* Sun Oct 12 2003 Peter Backlund <peter dot backlund at home dot se> - 0:1.0.4496-0.fdr.3
- Added NVidia configuration script written in Python.
- Some cleanup of files section
- For more info, see https://bugzilla.fedora.us/show_bug.cgi?id=402

* Tue Jul 08 2003 Andreas Bierfert (awjb) <andreas.bierfert[AT]awbsworld.de> - 0:1.0.4363-0.fdr.2
- renamed /sbin/makedevices.sh /sbin/nvidia-makedevices.sh ( noticed by
  Panu Matilainen )
- Fixed name problem
* Sun Jun 22 2003 Andreas Bierfert (awjb) <andreas.bierfert[AT]awbsworld.de> - 0:1.0.4363-0.fdr.1
- Initial RPM release, still some ugly stuff in there but should work...
