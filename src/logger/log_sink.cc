#include <logger.hh>

using namespace virtdb::interface;
using namespace std::placeholders;

namespace virtdb { namespace logger {
  
  log_sink::sptr log_sink::global_sink_;
  
}}
