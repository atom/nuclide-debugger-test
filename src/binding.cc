#include "nan.h"
#include "other-file.h"

using namespace v8;

static void SomeFunctionWrapper(const Nan::FunctionCallbackInfo<Value> &info) {
  int result = SomeFunction();
  info.GetReturnValue().Set(Nan::New<Number>(result));
}

void Init(Local<Object> exports, Local<Object> module) {
  // raise(SIGSTOP);
  module->Set(Nan::New("exports").ToLocalChecked(), Nan::New<FunctionTemplate>(SomeFunctionWrapper)->GetFunction());
}

NODE_MODULE(debugger_test, Init)
