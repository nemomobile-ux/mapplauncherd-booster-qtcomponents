TEMPLATE = app

TARGET = booster-nemomobile
QT += qml quick concurrent
qml.files = qml/preload.qml

CONFIG += qdeclarative-boostable link_pkgconfig

packagesExist(qdeclarative5-boostable) {
    message("Building with qdeclarative-boostable support")


    LIBS += -rdynamic -lmdeclarativecache5
    QMAKE_CXXFLAGS += -fPIC -fvisibility=hidden -fvisibility-inlines-hidden -I/usr/include/mdeclarativecache5

    QMAKE_PKGCONFIG_REQUIRES += qdeclarative5-boostable
} else {
    warning("qdeclarative-boostable not available; startup times will be slower")
}

target.path = /usr/libexec/mapplauncherd/
qml.path = /usr/share/$${TARGET}/

service.path = /usr/lib/systemd/user/
service.files = data/$${TARGET}.service

INSTALLS += target qml service

LIBS += -lapplauncherd
INCLUDEPATH += /usr/include/applauncherd/

SOURCES += src/qmlbooster.cpp src/eventhandler.cpp
HEADERS += src/qmlbooster.h src/eventhandler.h
OTHER_FILES += qml/preload.qml

