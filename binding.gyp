{
  "targets": [
    {
      "target_name": "debugger_test",
      "sources": [
        "src/binding.cc",
        "src/other-file.cc",
      ],

      "cflags_cc": ["-std=c++11"],

      "include_dirs": [
        "src",
        "<!(node -e \"require('nan')\")"
      ],

      "xcode_settings": {
        "OTHER_CPLUSPLUSFLAGS" : ["-std=c++11", "-stdlib=libc++"],
        "OTHER_LDFLAGS": ["-stdlib=libc++"],
        "MACOSX_DEPLOYMENT_TARGET": "10.9",
      }
    },
  ],
}
