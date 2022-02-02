<template>
  <div class='feed-frame'>
    <document-frame
      v-for='pdf in $data.pdfs'
      v-bind:key='pdf.fingerprint'
      v-bind:='pdf'
    ></document-frame>
  </div>
</template>

<script>
import DocumentFrame from './DocumentFrame.vue';

export default {
  data() {
    return {
      pdfs: [
        {
          title: 'Test in Action Of a Long Title A Test',
          fingerprint: 'e1980d94fa4685a388385b3010dc816db986afb7b6560f993d6ba58b72cddbdc',
          cover: 'http://0.0.0.0:9000/static/covers/freebsd_handbook.png',
        },
        {
          title: 'Rest in Action',
          fingerprint: 'e1980d94fa4685a388385b3010dc816db986afb7b6560f993d6ba58b72cddbdc',
          cover: 'http://0.0.0.0:9000/static/covers/Deep Learning.png',
        },
        {
          title: 'Test in Action',
          fingerprint: 'e1980d94fa4685a388385b3010dc816db986afb7b6560f993d6ba58b72cddbdc',
          cover:
            'http://0.0.0.0:9000/static/covers/IntroductoryCombinatorics.png',
        },
        {
          title: 'Test in Action',
          fingerprint: 4,
          cover: 'http://0.0.0.0:9000/static/covers/freebsd_handbook.png',
        },
        {
          title: 'Test in Action',
          fingerprint: 5,
          cover: 'http://0.0.0.0:9000/static/covers/freebsd_handbook.png',
        },
        {
          title: 'Test in Action',
          fingerprint: 6,
          cover: 'http://0.0.0.0:9000/static/covers/freebsd_handbook.png',
        },
        {
          title: 'Test in Action',
          fingerprint: 7,
          cover: 'http://0.0.0.0:9000/static/covers/freebsd_handbook.png',
        },
        {
          title: 'Test in Action',
          fingerprint: 7,
          cover: 'http://0.0.0.0:9000/static/covers/freebsd_handbook.png',
        },
        {
          title: 'Test in Action',
          fingerprint: 7,
          cover: 'http://0.0.0.0:9000/static/covers/freebsd_handbook.png',
        },
        {
          title: 'Test in Action',
          fingerprint: 7,
          cover: 'http://0.0.0.0:9000/static/covers/freebsd_handbook.png',
        },
        {
          title: 'Test in Action',
          fingerprint: 7,
          cover: 'http://0.0.0.0:9000/static/covers/freebsd_handbook.png',
        },
      ],
    };
  },
  name: 'TheDocumentFeed',
  components: {
    DocumentFrame,
  },
  props: {
    msg: String,
  },
};
</script>

<style scoped>
.feed-frame {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-content: space-around;
  justify-content: center;
  margin-left: 5%;
  margin-right: 5%;
}
</style>
