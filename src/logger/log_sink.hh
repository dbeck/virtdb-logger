#pragma once

#include <diag.pb.h>
#include <memory>

namespace virtdb { namespace logger {
  
  class log_sink
  {
  public:
    typedef std::shared_ptr<log_sink>                   sptr;
    typedef std::shared_ptr<interface::pb::LogRecord>   pb_logrec_sptr;
    
  private:
    log_sink(const log_sink &) = delete;
    log_sink & operator=(const log_sink &) = delete;
    
    static sptr global_sink_;
    
  public:
    log_sink() {}
    virtual ~log_sink() {}
    
    virtual bool send_record(pb_logrec_sptr rec) { return false; }
    static sptr get_sptr() { return global_sink_; }
    static void set_sptr(sptr sink) { global_sink_ = sink; }
  };
}}
