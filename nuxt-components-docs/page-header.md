<!-- source: https://ui.nuxt.com/components/page-header --> # PageHeaderPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PageHeader.vue)

A responsive header for your pages.

## Usage

The PageHeader component displays a header for your page.

Use it inside the default slot of the [Page](/components/page) component,
before the [PageBody](/components/page-body) component:

    
    
    <template>
      <UPage>
        <UPageHeader />
    
        <UPageBody />
      </UPage>
    </template>
    

### Title

Use the `title` prop to display a title in the header.

title

    
    
    <template>
      <UPageHeader title="PageHeader" />
    </template>
    

### Description

Use the `description` prop to display a description in the header.

description

    
    
    <template>
      <UPageHeader
        title="PageHeader"
        description="A responsive page header with title, description and actions."
      />
    </template>
    

### Headline

Use the `headline` prop to display a headline in the header.

headline

    
    
    <template>
      <UPageHeader
        title="PageHeader"
        description="A responsive page header with title, description and actions."
        headline="Components"
      />
    </template>
    

### Links

Use the `links` prop to display a list of [Button](/components/button) in the
header.

    
    
    <script setup lang="ts">
    const links = ref([
      {
        label: 'GitHub',
        icon: 'i-simple-icons-github',
        to: 'https://github.com/nuxt/ui-pro/tree/v3/src/runtime/components/PageHeader.vue',
        target: '_blank'
      }
    ])
    </script>
    
    <template>
      <UPageHeader
        title="PageHeader"
        description="A responsive page header with title, description and actions."
        headline="Components"
        :links="links"
      />
    </template>
    

## Examples

While these examples use [Nuxt Content](https://content.nuxt.com), the
components can be integrated with any content management system.

### Within a page

Use the PageHeader component in a page to display the header of the page:

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
        <UPageHeader
          :title="page.title"
          :description="page.description"
          :headline="page.headline"
          :links="page.links"
        />
    
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
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`title`| | ` string`  
`description`| | ` string`  
`links`| | ` ButtonProps[]`Display a list of Button next to the title. `{ color: 'neutral', variant: 'outline' }`Show properties

  * `label?: string`
  * `color?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`Defaults to `'primary'`.
  * `activeColor?: "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`
  * `variant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`Defaults to `'solid'`.
  * `activeVariant?: "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl"`Defaults to `'md'`.
  * `square?: boolean`Render the button with equal padding on all sides.
  * `block?: boolean`Render the button full width.
  * `loadingAuto?: boolean`Set loading state automatically based on the `@click` promise state
  * `class?: any`
  * `ui?: { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`
  * `icon?: string`Display an icon based on the `leading` and `trailing` props.
  * `avatar?: AvatarProps`Display an avatar on the left side.
  * `leading?: boolean`When `true`, the icon will be displayed on the left side.
  * `leadingIcon?: string`Display an icon on the left side.
  * `trailing?: boolean`When `true`, the icon will be displayed on the right side.
  * `trailingIcon?: string`Display an icon on the right side.
  * `loading?: boolean`When `true`, the loading icon will be displayed.
  * `loadingIcon?: string`The icon when the `loading` prop is `true`. Defaults to `appConfig.ui.icons.loading`.
  * `disabled?: boolean`
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.
  * `type?: "reset" | "submit" | "button"`The type of the button when not a link. Defaults to `'button'`.
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `active?: boolean`Force the link to be active independent of the current route.

  
`headline`| | ` string`  
`ui`| | ` { root?: ClassNameValue; container?: ClassNameValue; wrapper?: ClassNameValue; headline?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; links?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`headline`| `{}`  
`title`| `{}`  
`description`| `{}`  
`links`| `{}`  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pageHeader: {
          slots: {
            root: 'relative border-b border-default py-8',
            container: '',
            wrapper: 'flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4',
            headline: 'mb-2.5 text-sm font-semibold text-primary flex items-center gap-1.5',
            title: 'text-3xl sm:text-4xl text-pretty font-bold text-highlighted',
            description: 'text-lg text-pretty text-muted',
            links: 'flex flex-wrap items-center gap-1.5'
          },
          variants: {
            title: {
              true: {
                description: 'mt-4'
              }
            }
          }
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
            pageHeader: {
              slots: {
                root: 'relative border-b border-default py-8',
                container: '',
                wrapper: 'flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4',
                headline: 'mb-2.5 text-sm font-semibold text-primary flex items-center gap-1.5',
                title: 'text-3xl sm:text-4xl text-pretty font-bold text-highlighted',
                description: 'text-lg text-pretty text-muted',
                links: 'flex flex-wrap items-center gap-1.5'
              },
              variants: {
                title: {
                  true: {
                    description: 'mt-4'
                  }
                }
              }
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
            pageHeader: {
              slots: {
                root: 'relative border-b border-default py-8',
                container: '',
                wrapper: 'flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4',
                headline: 'mb-2.5 text-sm font-semibold text-primary flex items-center gap-1.5',
                title: 'text-3xl sm:text-4xl text-pretty font-bold text-highlighted',
                description: 'text-lg text-pretty text-muted',
                links: 'flex flex-wrap items-center gap-1.5'
              },
              variants: {
                title: {
                  true: {
                    description: 'mt-4'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[PageGridA responsive grid system for displaying content in a flexible
layout.](/components/page-grid)[PageHeroA responsive hero for your
pages.](/components/page-hero)

