{
  'variables': {
    'logger_sources': [
                        'src/logger/end_msg.hh',
                        'src/logger/header_store.cc',   'src/logger/header_store.hh',
                        'src/logger/log_record.cc',     'src/logger/log_record.hh',
                        'src/logger/log_sink.cc',       'src/logger/log_sink.hh',
                        'src/logger/macros.hh',
                        'src/logger/on_return.hh',
                        'src/logger/process_info.cc',   'src/logger/process_info.hh',
                        'src/logger/signature.cc',      'src/logger/signature.hh',
                        'src/logger/symbol_store.cc',   'src/logger/symbol_store.hh',
                        'src/logger/traits.hh',
                        'src/logger/variable.hh',
                        'src/logger.hh',
                      ],
    'logger_includes': [
                         './src/',
                         './deps_/proto/',
                         './deps_/utils/src/',
                         './deps_/',
                         '/usr/local/include/',
                         '/usr/include/',
                       ],
  },
  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'defines':  [ 'DEBUG', '_DEBUG', ],
        'cflags':   [ '-O0', '-g3', ],
        'ldflags':  [ '-g3', ],
        'xcode_settings': {
          'OTHER_CFLAGS':  [ '-O0', '-g3', ],
          'OTHER_LDFLAGS': [ '-g3', ],
        },
      },
      'Release': {
        'defines':  [ 'NDEBUG', 'RELEASE', ],
        'cflags':   [ '-O3', ],
        'xcode_settings': {
        },
      },
    },
    'include_dirs': [ '<@(logger_includes)' ],
    'cflags': [
                '-Wall',
                '-fPIC',
                '-std=c++11',
              ],
    'defines': [
                 'PIC',
                 'STD_CXX_11',
                 '_THREAD_SAFE',
                ],
  },
  'conditions': [
    ['OS=="mac"', {
     'defines':            [ 'LOGGER_MAC_BUILD', ],
     'xcode_settings':  {
       'GCC_ENABLE_CPP_EXCEPTIONS':    'YES',
       'OTHER_CFLAGS':               [ '-std=c++11', ],
     },},],
    ['OS=="linux"', {
     'defines':            [ 'LOGGER_LINUX_BUILD', ],
     'link_settings': {
       'ldflags':   [ '-Wl,--no-as-needed', ],
       'libraries': [ '-lrt', ],
     },},],
  ],
  'targets' : [
    {
      'conditions': [
        ['OS=="mac"', {
         'variables':  { 'logger_root':  '<!(pwd)/../', },
         'xcode_settings':  {
           'GCC_ENABLE_CPP_EXCEPTIONS':    'YES',
           'OTHER_CFLAGS':               [ '-std=c++11', ],
         },
         'direct_dependent_settings': {
           'include_dirs': [ '<(logger_root)/', ],
        },},],
        ['OS=="linux"', {
         'direct_dependent_settings': {
           'include_dirs':       [ '.', ],
        },},],
      ],
      'target_name':     'logger',
      'type':            'static_library',
      'defines':       [ 'USING_LOGGER_LIB',  ],
      'include_dirs':  [ '<@(logger_includes)', ],
      'sources':       [ '<@(logger_sources)', ],
    },
    {
      'target_name':       'logger_test',
      'type':              'executable',
      'dependencies':  [
                          'logger',
                          'deps_/gtest/gyp/gtest.gyp:gtest_lib',
                          'deps_/utils/utils.gyp:utils',
                          'deps_/proto/proto.gyp:*',
                       ],
      'include_dirs':  [
                          './deps_/gtest/include/',
                          '<@(logger_includes)',
                       ],
      'sources':       [ 'test/logger_test.cc', ],
    },
  ],
}
