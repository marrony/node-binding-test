{
  "targets": [{
    "target_name": "hello_native",
    "sources": [
      "binding.cpp"
    ],
    "include_dirs": [
      "<!@(node -p \"require('node-addon-api').include_dir\")"
    ],
    "cflags!": ["-fno-exceptions"],
    "cflags_cc!": ["-fno-exceptions"],
    "defines": ["NAPI_CPP_EXCEPTIONS"],
    'conditions': [
      ['OS=="win"',
        {
          'defines': ['CHECK_NODE_MODULE_VERSION'],
          'sources': [ ],
          'msvs_settings': {
            'VCCLCompilerTool': {
              'ExceptionHandling': '1',
              'DisableSpecificWarnings': [ '4530', '4506' ],
            }
          }
        }
      ],
      ['OS=="mac"',
        {
          'sources': [ ],
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'MACOSX_DEPLOYMENT_TARGET': '10.9',
            'OTHER_CFLAGS': [
              '-arch x86_64',
              '-arch arm64'
            ],
            'OTHER_LDFLAGS': [
              '-framework CoreFoundation',
              '-framework IOKit',
              '-arch x86_64',
              '-arch arm64'
            ]
          }
        }
      ],
      ['OS=="linux"',
        {
          'sources': [ ]
        }
      ],
      ['OS=="android"',
        {
          'sources': [ ]
        }
      ],
      ['OS!="win"',
        {
          'sources': [ ]
        }
      ]
    ]
  }],
}
