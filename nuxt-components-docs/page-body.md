<!-- source: https://ui.nuxt.com/components/page-body --> # PageBodyPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PageBody.vue)

The main content of your page.

## Usage

The PageBody component wraps your main content and adds some padding for
consistent spacing.

Use it inside the default slot of the [Page](/components/page) component,
after the [PageHeader](/components/page-header) component:

    
    
    <template>
      <UPage>
        <UPageHeader />
    
        <UPageBody />
      </UPage>
    </template>
    

## Examples

While these examples use [Nuxt Content](https://content.nuxt.com), the
components can be integrated with any content management system.

### Within a page

Use the PageBody component in a page to display the content of the page:

pages/[...slug].vue

    
    
    <script setup lang="ts">
    const route = useRoute()
    
    definePageMeta({
      layout: 'docs'
    })
    
    const { data: page } = await useAsyncData(route.path, () => {
      return queryCollection('content').path(route.path).first()
    })
    
    const { data: surround } = await useAsyncData(`${route.path}-surround`, () => {
      return queryCollectionItemSurroundings('content', route.path)
    })
    </script>
    
    <template>
      <UPage>
        <UPageHeader :title="page.title" :description="page.description" />
    
        <UPageBody>
          <ContentRenderer :value="page" />
    
          <USeparator />
    
          <UContentSurround :surround="surround" />
        </UPageBody>
    
        <template #right>
          <UContentToc :links="page.body.toc.links" />
        </template>
      </UPage>
    </template>
    

In this example, we use the
[`ContentRenderer`](https://content.nuxt.com/docs/components/content-renderer)
component from `@nuxt/content` to render the content of the page.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pageBody: {
          base: 'mt-8 pb-24 space-y-12'
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          uiPro: {
            pageBody: {
              base: 'mt-8 pb-24 space-y-12'
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          uiPro: {
            pageBody: {
              base: 'mt-8 pb-24 space-y-12'
            }
          }
        })
      ]
    })
    

Expand code

[PageAsideA sticky aside to display your page navigation.](/components/page-
aside)[PageCardA pre-styled card component that displays a title, description
and optional link.](/components/page-card)

